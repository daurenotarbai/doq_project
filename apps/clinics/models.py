import datetime
from decimal import Decimal

from django.contrib.auth.models import User
from django.core import exceptions
from django.db import models
from django.db.models import TextChoices
from django.utils.safestring import mark_safe
from django_admin_geomap import GeoItem

from apps.core.models import TimestampMixin, ContactMixin, City


class Gender(TextChoices):
    MALE = "MALE", "Мужской"
    FEMALE = "FEMALE", "Женский"


class AgeChoices(TextChoices):
    ZERO = "0 мес.", "0 мес."
    ONE_MONTH = "1 мес.", "1 мес."
    TWO_MONTH = "2 мес.", "2 мес."
    THREE_MONTH = "3 мес.", "3 мес."
    FOUR_MONTH = "4 мес.", "4 мес."
    FIVE_MONTH = "5 мес.", "5 мес."
    SIX_MONTH = "6 мес.", "6 мес."
    SEVEN_MONTH = "7 мес.", "7 мес."
    EIGHT_MONTH = "8 мес.", "8 мес."
    NINE_MONTH = "9 мес.", "9 мес."
    TEN_MONTH = "10 мес.", "10 мес."
    ELEVEN_MONTH = "11 мес.", "11 мес."
    ONE = "1 год", "1 год"
    TWO = "2 года", "2 года"
    THREE = "3 года", "3 года"
    FOUR = "4 года", "4 года"
    FIVE = "5 лет", "5 лет"
    SIX = "6 лет", "6 лет"
    SEVEN = "7 лет", "7 лет"
    EIGHT = "8 лет", "8 лет"
    NINE = "9 лет", "9 лет"
    TEN = "10 лет", "10 лет"
    ELEVEN = "11 лет", "11 лет"
    TWELVE = "12 лет", "12 лет"
    THIRTEEN = "13 лет", "13 лет"
    FOURTEEN = "14 лет", "14 лет"
    FIFTEEN = "15 лет", "15 лет"
    SIXTEEN = "16 лет", "16 лет"
    SEVENTEEN = "17 лет", "17 лет"
    EIGHTEEN = "18 лет", "18 лет"


# class DoctorCategory(TextChoices):
#     DOCTOR = "Врач"
#     ACADEMIC = "Академик"
#     PROFESSOR = "Провессор"
#     MASTER = "Магистр"
#     MASTER_DOC = "Магистр здравоохранения"
#     RESIDENT = "Резидент"
#     NURSE = "Медсестра (Медбрат)"
#     CANDIDATE = "Кандидат медицинских наук"
#     DOC_CANDIDATE = "Доктор медицинских наук"
#     SPECIALIST = "Специалист"
#     PHD = "PhD"
#     FIRST = "Врач первый категории"
#     SECOND = "Врач второй категории"
#     HIGHER = "Врач высшей категории"


class WeekDays(TextChoices):
    MONDAY = "MONDAY", "Понедельник"
    TUESDAY = "TUESDAY", "Вторник"
    WEDNESDAY = "WEDNESDAY", "Среда"
    THURSDAY = "THURSDAY", "Четверг"
    FRIDAY = "FRIDAY", "Пятница"
    SATURDAY = "SATURDAY", "Суббота"
    SUNDAY = "SUNDAY", "Воскресенье"


WeekDaysNumber = {
    'MONDAY': 0,
    'TUESDAY': 1,
    'WEDNESDAY': 2,
    'THURSDAY': 3,
    'FRIDAY': 4,
    'SATURDAY': 5,
    'SUNDAY': 6,
}


def clinic_photo_path(instance, filename):
    return "photos/clinic/{0}/{1}".format(instance.id, filename)


def doctor_application_photo_path(instance, filename):
    return "photos/doctor/application/photos".format(instance.id, filename)


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

    name = models.CharField(
        'Название клиники',
        max_length=50,
        default='')
    description = models.TextField(
        "Описание",
        blank=True,
        default='',
        help_text="Подробное описание")
    short_description = models.CharField(
        'Краткое описание',
        max_length=120,
        default='')
    logo = models.ImageField(
        "Лого клиники",
        upload_to=clinic_photo_path,
        blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Пользователь",
        related_name='clinic',
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True
    )
    is_active = models.BooleanField(
        'Актив',
        default=True,
        blank=True)

    def image_tag(self):
        if self.logo:
            return mark_safe('<img src="{}" width="100" />'.format(self.logo.url))
        return 'Фото еще не загрузили'

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class ClinicImage(models.Model):
    class Meta:
        verbose_name = "Фото клиники"
        verbose_name_plural = "Фотографии клиники"

    image = models.ImageField(
        "Файл с изображением",
        upload_to=clinic_photo_path,
        null=True,
    )
    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name="images",
    )
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        for image_model in self.clinic.images.all():
            if image_model.is_main and self.is_main:
                raise exceptions.BadRequest('main image already exist ')
        super().save(*args, **kwargs)


class Address(models.Model, GeoItem):
    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    address = models.CharField(
        'Адресс',
        max_length=255,
        null=True,
        blank=True,
    )
    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name="addresses",
    )
    is_24_hours = models.BooleanField(
        'Круглосуточно',
        default=False,
        blank=True,
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    @property
    def geomap_popup_view(self):
        return "<strong>{}</strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view

    @property
    def geomap_longitude(self):
        return str(self.longitude)

    @property
    def geomap_icon(self):
        return self.default_icon

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    def __str__(self) -> str:
        return self.address


class Schedules(models.Model):
    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписании"
        unique_together = ['day_in_week', 'address']

    day_in_week = models.CharField('День недели', choices=WeekDays.choices, max_length=255,
                                   null=True, blank=True)
    start_day = models.TimeField(null=True, blank=True)
    end_day = models.TimeField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="schedules")

    def __str__(self) -> str:
        return f'{self.day_in_week}'


class DoctorCategory(models.Model):
    name = models.CharField(
        "Названия категории",
        max_length=255,
        default='',
    )

    class Meta:
        verbose_name = 'Категория доктора'
        verbose_name_plural = 'Категории доктора'

    def __str__(self):
        return f'{self.name}'


class Doctor(TimestampMixin):
    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Докторы'

    first_name = models.CharField(
        "Имя",
        max_length=255,
        default='',
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=255,
        default='',
    )
    middle_name = models.CharField(
        "Отчество",
        max_length=255,
        blank=True,
        default='',
    )
    description = models.TextField(
        "Описание",
        blank=True,
        default='',
        help_text="Подробное описание",
    )
    photo = models.ImageField(
        "Фото специалиста",
        upload_to=specialist_photo_path,
        null=True,
        blank=True,
    )
    gender = models.CharField(
        'Пол',
        max_length=10,
        choices=Gender.choices,
        blank=True,
        null=True,
    )
    operates_from = models.DateField(
        "Работает с",
    )

    consultation_fee = models.DecimalField(
        'Цена за прием',
        max_digits=10,
        decimal_places=2,
        default=Decimal(0),
    )
    discount_consultation_fee = models.PositiveIntegerField(
        'Скидка на стоимость приема',
        default=0,
    )
    new_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal(0),
    )
    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name="doctors",
        verbose_name="Клиника",
    )
    specialities = models.ManyToManyField(
        Speciality, verbose_name="Специальности",
        related_name="doctors",
        through='DoctorSpecialities',
    )
    procedures = models.ManyToManyField(
        Procedure,
        verbose_name="Процедуры",
        related_name='doctors',
        through='DoctorProcedures',
    )
    score = models.FloatField(
        'Рейтинг',
        default=0.0,
    )
    for_child = models.BooleanField(
        'Детский',
        default=True,
        blank=True,
    )
    is_active = models.BooleanField(
        'Активный',
        default=True,
        blank=True,
    )
    categories = models.ManyToManyField(
        DoctorCategory,
        verbose_name="Категории доктора",
        blank=True,
    )

    def image_tag(self):
        if self.photo:
            return mark_safe(
                '<img src="{}" style="border-radius:10%" width="120" />'.format(self.photo.url))
        return "Фото не загрузил"

    @property
    def experience_years(self):
        experience = datetime.datetime.now().date().year - self.operates_from.year
        return experience

    image_tag.short_description = 'Фото'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DoctorProcedures(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='doctor_procedures',
        verbose_name="Доктор",
    )
    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.CASCADE,
        related_name='doctor_procedures',
        verbose_name="Процедура",

    )
    price = models.DecimalField(
        verbose_name="Цена приема",
        max_digits=10,
        decimal_places=2,
        default=Decimal(0),
    )
    discount = models.PositiveIntegerField(
        default=0,
        verbose_name="Скидка",
    )
    for_child = models.BooleanField(
        'Детский',
        default=True,
        blank=True,
        null=True
    )
    child_price = models.DecimalField(
        verbose_name="Цена приема (Детский)",
        max_digits=10,
        decimal_places=2,
        default=Decimal(0),
    )
    child_discount = models.PositiveIntegerField(
        default=0,
        verbose_name="Скидка (Детский)",
    )
    new_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal(0),
    )
    child_age_from = models.CharField('Возраст детей от', choices=AgeChoices.choices,
                                      max_length=255,
                                      null=True, blank=True,
                                      )
    child_age_to = models.CharField('Возраст детей до', choices=AgeChoices.choices,
                                    max_length=255,
                                    null=True, blank=True,
                                    )


class DoctorSpecialities(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='doctor_specialities',
        verbose_name="Доктор",
    )
    speciality = models.ForeignKey(
        Speciality,
        on_delete=models.CASCADE,
        related_name='doctor_specialities',
        verbose_name="Специальность",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal(0),
        verbose_name="Цена приема",
    )
    discount = models.PositiveIntegerField(
        default=0,
        verbose_name="Скидка",
    )
    for_child = models.BooleanField(
        'Детский',
        default=True,
        blank=True,
        null=True
    )
    child_price = models.DecimalField(
        verbose_name="Цена приема (Детский)",
        max_digits=10,
        decimal_places=2,
        default=Decimal(0),
    )
    child_discount = models.PositiveIntegerField(
        default=0,
        verbose_name="Скидка (Детский)",
    )
    new_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal(0),
    )
    child_age_from = models.CharField('Возраст детей от', choices=AgeChoices.choices,
                                      max_length=255,
                                      null=True, blank=True,
                                      )
    child_age_to = models.CharField('Возраст детей до', choices=AgeChoices.choices,
                                    max_length=255,
                                    null=True, blank=True,
                                    )


class AppointmentDoctorTime(models.Model):
    class Meta:
        verbose_name = 'Времени на прием'
        verbose_name_plural = 'Времени на прием'
        unique_together = ('doctor', 'date', 'clinic_address',)

    clinic_address = models.ForeignKey(
        Address, on_delete=models.CASCADE,
        null=True,
        verbose_name="Адрес клиники",
        related_name="appoint_times",
    )
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


class ClinicApplication(TimestampMixin):
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    name_clinic = models.CharField(
        'Название клиники',
        max_length=200,
        null=True,
        blank=True,
    )
    name = models.CharField(
        'Имя клиента',
        max_length=200,
        null=True,
        blank=True,
    )
    city = models.CharField(
        'Город',
        max_length=30,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        'Номер телефона',
        max_length=15,
        null=True,
        blank=True,
    )
    doctor_name = models.CharField(
        'Номер телефона',
        max_length=50,
        null=True,
        blank=True,
    )
    from_doctor = models.BooleanField(
        'От Доктора',
        default=False,
        blank=True,
        null=True
    )
    speciality = models.CharField(
        'Специальность',
        max_length=200,
        null=True,
        blank=True,
    )
    experience_years = models.CharField(
        'Опыт работы',
        max_length=200,
        null=True,
        blank=True,
    )
    institution = models.CharField(
        'Учебное заведение',
        max_length=200,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        "Фото доктора",
        upload_to=doctor_application_photo_path,
        blank=True,
    )

    def image_tag(self):
        if self.image:
            return mark_safe(
                '<img src="{}" style="border-radius:10%" width="120" />'.format(self.image.url))
        return "Фото не загрузил"

    image_tag.short_description = 'Фото'

    def __str__(self):
        return f'{self.name_clinic} - {self.created_at}'
