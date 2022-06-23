from datetime import datetime, timedelta

from django.contrib import admin

from apps.clinics.models import AppointmentTime, Doctor, Clinic, Address, Speciality, Procedure, AppointmentDoctorTime
from apps.core.admin import OnlySuperUserMixin, NoAddMixin, NoDeleteMixin, NoViewMixin


class AddressClinicInline(admin.TabularInline):
    model = Address
    extra = 0


class DoctorsInline(admin.TabularInline):
    model = Doctor
    fields = ['first_name', 'last_name', 'experience_years', 'consultation_fee']
    extra = 1


class DoctorsAppoinmentTimeInline(admin.TabularInline):
    model = AppointmentDoctorTime
    fields = ['date', 'times']
    readonly_fields = ('date',)
    extra = 0


@admin.register(Clinic)
class ClinicAdmin(OnlySuperUserMixin, NoAddMixin, NoDeleteMixin, admin.ModelAdmin):
    list_display = ("image_tag", "name", "phone")
    fieldsets = (
        ('', {'fields': (('image_tag', 'logo'),)}),
        ('Основная информация', {
            'fields': (('name', 'phone'), 'description')
        }),
    )
    readonly_fields = ['image_tag']
    inlines = [AddressClinicInline, DoctorsInline]

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


@admin.register(Doctor)
class DoctorAdmin(OnlySuperUserMixin, NoAddMixin, NoDeleteMixin, admin.ModelAdmin):
    list_display = (
        "image_tag", "first_name", "last_name", "clinic", "get_specialities", "get_procedures", "get_todays_times",
        "get_tomorrows_times")
    fieldsets = (
        ('', {'fields': (('image_tag', 'photo'),)}),
        ('Основная информация', {
            'fields': (('first_name', 'last_name'), ('middle_name', 'gender'),
                       ('experience_years', 'consultation_fee'), 'clinic')
        }),
        ('По специальности', {'fields': ('specialities', 'procedures',)}),

    )
    readonly_fields = ('image_tag', 'clinic')
    inlines = [DoctorsAppoinmentTimeInline, ]
    filter_horizontal = ('procedures', "specialities")
    search_fields = ['first_name',"last_name","clinic__name"]
    def create_appointmen_times(self, obj):
        doctor = Doctor.objects.get(id=obj.id)
        appointment_doctor_time = []
        for item in range(5):
            appointment_doctor_time.append(
                AppointmentDoctorTime(date=datetime.now().date() + timedelta(days=item), doctor=doctor))

        AppointmentDoctorTime.objects.bulk_create(appointment_doctor_time, ignore_conflicts=True)

    def get_specialities(self, obj):
        self.create_appointmen_times(obj)
        return " | ".join([s.name for s in obj.specialities.all()])

    def get_procedures(self, obj):
        return " | ".join([s.name for s in obj.procedures.all()])

    def get_todays_times(self, obj):
        doctor_appointment = obj.appoint_times.filter(date=datetime.now().date()).first()
        times = [times.start_time.strftime('%H:%M') for times in doctor_appointment.times.all()]
        return " | ".join(times)

    def get_tomorrows_times(self, obj):
        doctor_appointment = obj.appoint_times.filter(date=datetime.now().date() + timedelta(days=1)).first()
        times = [times.start_time.strftime('%H:%M') for times in doctor_appointment.times.all()]
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
