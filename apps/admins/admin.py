import datetime

from django.contrib import admin
from django.db import IntegrityError
from django_object_actions import DjangoObjectActions

from apps.admins.models import MonthReport
from apps.clinics.models import Address
from apps.core.admin import NoAddMixin
from apps.patients.models import Appointment


@admin.register(MonthReport)
class MonthReportAdmin(NoAddMixin, DjangoObjectActions, admin.ModelAdmin):
    list_display = (
    'month', 'verified', 'total_appointments', 'status', 'address', 'get_clinic_name')
    ordering = ['month']

    def check_current_month(modeladmin, request, queryset):
        addresses = Address.objects.all()
        today = datetime.datetime.today()
        for address in addresses:
            appointments = Appointment.objects.filter(appointment_doctor_time__clinic_address=address, appointment_doctor_time__date__month=today.month)
            verified = appointments.filter(is_visited=True)
            try:
                MonthReport.objects.update_or_create(month=today, address=address, defaults={
            'total_appointments': appointments.count,
            'verified': verified.count,
        })
            except IntegrityError:
                pass

    def check_previous_month(modeladmin, request, queryset):
        addresses = Address.objects.all()
        today = datetime.datetime.today()
        first = today.replace(day=1)
        last_month = first - datetime.timedelta(days=1)
        for address in addresses:
            appointments = Appointment.objects.filter(appointment_doctor_time__clinic_address=address, appointment_doctor_time__date__month=last_month.month)
            verified = appointments.filter(is_visited=True)
            try:
                MonthReport.objects.update_or_create(month=last_month, address=address, defaults={
            'total_appointments': appointments.count,
            'verified': verified.count,
        })
            except IntegrityError:
                pass

    check_current_month.label = "Сверить текущий месяц"
    check_current_month.short_description = "Сверить текущий месяц"
    changelist_actions = ('check_previous_month', 'check_current_month')
    check_previous_month.label = "Сверить предыдущий месяц"
    check_previous_month.short_description = "Сверить предыдущий месяц"

    def get_clinic_name(self, obj):
        return obj.address.clinic.name

    get_clinic_name.short_description = "Клиника"
