from django.contrib import admin

from apps.admins.models import MonthReport


@admin.register(MonthReport)
class MonthReportAdmin(admin.ModelAdmin):
    list_display = ('month', 'verified', 'total_appointments', 'status')
