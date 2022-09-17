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
    verified = models.PositiveIntegerField("Сверенных", default=0)
    total_appointments = models.PositiveIntegerField("Всего заявок", default=0)
    status = models.CharField("Статус", max_length=12, choices=Status.choices, default=Status.UNPAID.value)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, verbose_name="Адрес", null=True)

    def __str__(self):
        return f'{self.month}'
