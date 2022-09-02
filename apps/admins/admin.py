from django.contrib import admin

from apps.admins.models import MonthReport

@admin.action(description='Сверка')
def make_month_reconciliation(modeladmin, request, queryset):
    # queryset.update(status='p')
    pass

@admin.register(MonthReport)
class MonthReportAdmin(admin.ModelAdmin):
    list_display = ('month', 'verified', 'total_appointments', 'status')
    ordering = ['month']
    actions = [make_month_reconciliation]
