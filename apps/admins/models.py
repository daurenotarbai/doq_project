from django.db import models
from django.db.models import TextChoices

from apps.clinics.models import Address
from apps.core.models import TimestampMixin


class Status(TextChoices):
    DONE = "DONE", "сдана"
    PAID = "PAID", "оплачено"
    UNPAID = "UNPAID", "сверка"


class MonthReport(TimestampMixin):
    class Meta:
        verbose_name = 'Сверка'
        verbose_name_plural = 'Сверка'
        unique_together = ['month', 'address']

    month = models.DateField(verbose_name='Месяц')
    verified = models.PositiveIntegerField(default=0)
    total_appointments = models.PositiveIntegerField(default=0)
    status = models.CharField("Номер телефона", max_length=12, choices=Status.choices)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.month}'
