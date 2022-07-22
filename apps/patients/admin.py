from django.contrib import admin

from apps.core.admin import NoAddMixin
from apps.patients.models import Appointment, Patient, Comment


class AppointmentAdmin(NoAddMixin, admin.ModelAdmin):
    list_display = ("id", "patient", "appointment_time")


admin.site.register(Appointment, AppointmentAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "created_at")


admin.site.register(Patient, PatientAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "patient", "text", "doctor")


admin.site.register(Comment, CommentAdmin)
