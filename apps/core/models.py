from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField("Время создания", auto_now_add=True, db_index=True)
    changed_at = models.DateTimeField("Время последнего изменения", auto_now=True, db_index=True)

    class Meta:
        abstract = True


class ContactMixin(models.Model):
    class Meta:
        abstract = True

    phone = models.CharField("Мобильный телефон", max_length=20, default='')
    work_phone = models.CharField("Рабочий телефон", max_length=20, default='')
