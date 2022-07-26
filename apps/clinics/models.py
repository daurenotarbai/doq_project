from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextChoices
from django.utils.safestring import mark_safe

from apps.core.models import TimestampMixin, ContactMixin


class Gender(TextChoices):
    MALE = "MALE", "Мужской"
    FEMALE = "FEMALE", "Женский"


def clinic_photo_path(instance, filename):
    return "photos/clinic/{0}/{1}".format(instance.id, filename)


def specialist_photo_path(instance, filename):
    return "photos/clinic/{}/specialist/{}/{}".format(instance.clinic.id, instance.id, filename)


class AppointmentTime(models.Model):
    class Meta:
        verbose_name = 'Интервал времени'
        verbose_name_plural = 'Интервалы времени'

    start_time = models.TimeField(verbose_name='Время начало приема')

    def __str__(self):
        start_time = self.start_time.strftime('%H:%M')
        return f'{start_time}'


class Speciality(models.Model):
    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ("name",)

    name = models.CharField("Название специальности", max_length=255, default='')

    def __str__(self):
        return f'{self.name}'


class Procedure(models.Model):
    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'
        ordering = ("name",)

    name = models.CharField("Название процедуры", max_length=255, default='')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name="subprocedures")
    is_specialty = models.BooleanField('По специальности', default=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Clinic(TimestampMixin, ContactMixin):
    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'

    name = models.CharField('Название клиники', max_length=50, default='')
    description = models.TextField("Описание", blank=True, default='',
                                   help_text="Подробное описание")
    logo = models.ImageField("Лого клиники", upload_to=clinic_photo_path, blank=True)
    image = models.ImageField("Файл с изображением", upload_to=clinic_photo_path, null=True,
                              blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Пользователь",
                             related_name='clinic',
                             )
    is_active = models.BooleanField('Актив', default=True, blank=True)

    def image_tag(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.logo.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class Address(models.Model):
    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    city = models.CharField('Город', max_length=255, null=True, blank=True)
    address = models.CharField('Адресс', max_length=255, null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="addresses")

    def __str__(self) -> str:
        return self.address


# class DoctorDescriptionMixin(models.Model):
#     class Meta:
#         abstract = True
#     description = models.TextField("Описание", blank=True, default='', help_text="Подробное описание")
#     education = models.CharField("Образование", max_length=20, default='')
#     courses = models.CharField("Курсы", max_length=20, default='')


class Doctor(TimestampMixin):
    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Докторы'

    first_name = models.CharField("Имя", max_length=255, default='')
    last_name = models.CharField("Фамилия", max_length=255, default='')
    middle_name = models.CharField("Отчество", max_length=255, blank=True, default='')
    description = models.TextField("Описание", blank=True, default='',
                                   help_text="Подробное описание")
    photo = models.ImageField("Фото специалиста", upload_to=specialist_photo_path, null=True,
                              blank=True)
    gender = models.CharField('Пол', max_length=10, choices=Gender.choices, blank=True, null=True)
    experience_years = models.PositiveSmallIntegerField('Опыт работы', null=True, default=1)
    consultation_fee = models.DecimalField('Цена за прием', max_digits=10, decimal_places=2,
                                           default=Decimal(0))
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="doctors",
                               verbose_name="Клиника")
    specialities = models.ManyToManyField(Speciality, verbose_name="Специальности",
                                          related_name="doctors")
    procedures = models.ManyToManyField(Procedure, verbose_name="Процедуры", related_name='doctors',
                                        through='DoctorProcedures')
    score = models.FloatField('Рейтинг', default=0.0)
    for_child = models.BooleanField('Детский', default=True, blank=True)

    def image_tag(self):
        if self.photo:
            return mark_safe(
                '<img src="{}" style="border-radius:10%" width="120" />'.format(self.photo.url))
        return "Фото не загрузил"

    image_tag.short_description = 'Фото'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DoctorProcedures(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='doctor_procedures')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                default=Decimal(0))


class AppointmentDoctorTime(models.Model):
    class Meta:
        verbose_name = 'Времени на прием'
        verbose_name_plural = 'Времени на прием'
        unique_together = ('doctor', 'date')

    clinic_address = models.ForeignKey(
        Address, on_delete=models.CASCADE,
        null=True,
        verbose_name="Адрес клиники",
        related_name="appoint_times")
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Доктор",
        related_name="appoint_times",
    )
    times = models.ManyToManyField(
        AppointmentTime,
        verbose_name="Времени на прием",
        blank=True,
    )
    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        return f'{self.doctor} - {self.date}'
