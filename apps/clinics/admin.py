from datetime import datetime, timedelta
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django_admin_geomap import ModelAdmin as GeOModelAdmin

from apps.clinics.models import Doctor, Clinic, Address, Speciality, Procedure, \
    AppointmentDoctorTime, Schedules, ClinicApplication, ClinicImage
from apps.core.admin import OnlySuperUserMixin, NoAddMixin, NoDeleteMixin
from django.utils.translation import gettext_lazy as _

class MyDateTimeFilter(admin.DateFieldListFilter):
    def __init__(self, *args, **kwargs):
        super(MyDateTimeFilter, self).__init__(*args, **kwargs)

        now = timezone.now()
        # When time zone support is enabled, convert "now" to the user's time
        # zone so Django's definition of "Today" matches what the user expects.
        if timezone.is_aware(now):
            now = timezone.localtime(now)

        today = now.date()

        self.links += ((
            (_('Next 7 days'), {
                self.lookup_kwarg_since: str(today),
                self.lookup_kwarg_until: str(today + timedelta(days=7)),
            }),
        ))


class AddressClinicInline(admin.TabularInline):
    model = Address
    extra = 0


class DoctorsInline(admin.TabularInline):
    model = Doctor
    fields = ['first_name', 'last_name', 'operates_from', 'consultation_fee']
    extra = 1


@admin.register(AppointmentDoctorTime)
class DoctorsAppointmentTimeAdmin(admin.ModelAdmin):
    model = AppointmentDoctorTime
    fields = ['doctor', 'date', 'times', 'clinic_address']
    list_display = ['doctor', 'date', 'clinic_address', 'get_times']
    filter_horizontal = ('times',)
    list_filter = [
        'doctor', 'clinic_address', 'clinic_address__clinic', ('date', MyDateTimeFilter)]

    def get_times(self, obj):
        times = [times.start_time.strftime('%H:%M') for times in obj.times.all()]
        return " | ".join(times)

    get_times.short_description = "Времени"

    def get_queryset(self, request):
        qs = super(DoctorsAppointmentTimeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            self.list_filter = ['doctor', ('date', MyDateTimeFilter)]
            return qs.filter(doctor__clinic__user=request.user)

    def render_change_form(self, request, context, *args, **kwargs):
        if not request.user.is_superuser:
            context['adminform'].form.fields['clinic_address'].queryset = Address.objects.filter(
                clinic__user=request.user)
            context['adminform'].form.fields['doctor'].queryset = Doctor.objects.filter(
                clinic__user=request.user)
        return super(DoctorsAppointmentTimeAdmin, self).render_change_form(request, context, *args,
                                                                           **kwargs)


@admin.register(Clinic)
class ClinicAdmin(OnlySuperUserMixin, NoAddMixin, NoDeleteMixin, SummernoteModelAdmin):
    list_display = ("image_tag", "name", "phone", 'user',)
    fieldsets = (
        ('', {'fields': (('image_tag', 'logo'),)}),
        ('Основная информация', {
            'fields': (('name', 'phone', 'user'), 'description')
        }),
    )
    readonly_fields = ['image_tag']
    inlines = [AddressClinicInline, DoctorsInline]
    summernote_fields = ('description', )

    def get_queryset(self, request):
        qs = super(ClinicAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


class ProcedureInlineAdmin(admin.TabularInline):
    model = Doctor.procedures.through


class SpecialityInlineAdmin(admin.TabularInline):
    model = Doctor.specialities.through


@admin.register(Doctor)
class DoctorAdmin(OnlySuperUserMixin, NoAddMixin, NoDeleteMixin, SummernoteModelAdmin):
    list_display = (
        "image_tag", "first_name", "last_name", "clinic", "get_specialities", "get_procedures",
        "get_todays_times",
        "get_tomorrows_times")
    fieldsets = (
        ('', {'fields': (('image_tag', 'photo'),)}),
        ('Основная информация', {
            'fields': (('first_name', 'last_name'), ('middle_name', 'gender', 'is_active'),
                       ('operates_from', 'consultation_fee', 'for_child'), 'clinic', 'achievements',
                       'category', 'description')
        }),

    )
    readonly_fields = ('image_tag', 'clinic')
    inlines = [ProcedureInlineAdmin, SpecialityInlineAdmin]
    filter_horizontal = ('procedures', "specialities")
    search_fields = ['first_name', "last_name", "clinic__name"]
    summernote_fields = ('description',)

    def get_specialities(self, obj):
        return " | ".join([s.name for s in obj.specialities.all()])

    def get_procedures(self, obj):
        return " | ".join([s.name for s in obj.procedures.all()])

    def get_todays_times(self, obj):
        doctor_appointment = obj.appoint_times.filter(date=datetime.now().date()).first()
        if doctor_appointment:
            times = [times.start_time.strftime('%H:%M') for times in doctor_appointment.times.all()]
        else:
            times = ""
        return " | ".join(times)

    def get_tomorrows_times(self, obj):
        doctor_appointment = obj.appoint_times.filter(
            date=datetime.now().date() + timedelta(days=1)).first()
        if doctor_appointment:
            times = [times.start_time.strftime('%H:%M') for times in doctor_appointment.times.all()]
        else:
            times = ""
        return " | ".join(times)

    get_procedures.short_description = "Процедуры"
    get_specialities.short_description = "Специальности"
    get_tomorrows_times.short_description = "Завтра"
    get_todays_times.short_description = "Сегодня"

    def get_queryset(self, request):
        qs = super(DoctorAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            self.list_filter = ['clinic', ]
            return qs
        self.list_filter = []
        return qs.filter(clinic__user=request.user)


class ScheduleInlineAdmin(admin.TabularInline):
    model = Schedules
    extra = 0


class AddressAdmin(NoAddMixin, GeOModelAdmin):
    list_display = ['city', 'address', 'is_24_hours', 'get_schedules']
    inlines = (ScheduleInlineAdmin,)

    def get_schedules(self, obj):
        return format_html("".join(
            ['{} : {} - {}<br>'.format(s.day_in_week, s.start_day, s.end_day) for s in
             obj.schedules.all()]))

    def get_queryset(self, request):
        qs = super(AddressAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            self.list_filter = ['clinic', ]
            return qs
        else:
            self.list_filter = []
        return qs.filter(clinic__user=request.user)

    geomap_field_longitude = "id_longitude"
    geomap_field_latitude = "id_latitude"
    geomap_default_longitude = "76.8512"
    geomap_default_latitude = "43.223"
    geomap_default_zoom = "10"


admin.site.register(Address, AddressAdmin)


@admin.register(ClinicApplication)
class ClinicApplicationAdmin(NoAddMixin, admin.ModelAdmin):
    list_display = ('name_clinic', 'name', 'created_at')


@admin.register(ClinicImage)
class ClinicImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'clinic', 'is_main')
