from django.contrib import admin

from apps.clinics.admin import MyDateTimeFilter
from apps.clinics.models import AppointmentDoctorTime
from apps.patients.models import Appointment, Patient, Comment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id", "patient", "appointment_time", 'get_date', "get_doctor",
    )
    list_filter = [('appointment_doctor_time__date', MyDateTimeFilter)]

    def render_change_form(self, request, context, *args, **kwargs):
        if not request.user.is_superuser:
            context['adminform'].form.fields[
                'appointment_doctor_time'].queryset = AppointmentDoctorTime.objects.filter(
                doctor__clinic__user=request.user)
        return super(AppointmentAdmin, self).render_change_form(request, context, *args,
                                                                **kwargs)

    def get_doctor(self, obj):
        if obj.doctor_procedure:
            return obj.doctor_procedure.doctor
        elif obj.doctor_specialities:
            return obj.doctor_speciality.doctor

    def get_date(self, obj):
        if not obj.appointment_doctor_time:
            return 'Будет согласованы с клиникой'
        return obj.appointment_doctor_time.date

    get_doctor.short_description = 'Доктор'
    get_date.short_description = 'День'


admin.site.register(Appointment, AppointmentAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "created_at")


admin.site.register(Patient, PatientAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "text", "doctor")


admin.site.register(Comment, CommentAdmin)
