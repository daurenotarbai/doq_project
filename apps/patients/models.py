from django.core import exceptions
from django.db import models

from apps.clinics.models import AppointmentTime, Doctor, AppointmentDoctorTime, DoctorProcedures, \
    DoctorSpecialities
from apps.core.models import TimestampMixin


class Patient(TimestampMixin):
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    phone = models.CharField("Номер телефона", max_length=12)
    first_name = models.CharField("Имя", max_length=255, blank=True, default='')
    iin = models.CharField("ЖСН", max_length=12, blank=True, default='', unique=True)

    def __str__(self):
        return f'{self.first_name}-{self.iin}'


class Appointment(TimestampMixin):
    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'
        unique_together = ['appointment_time', 'appointment_doctor_time']

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments",
                                null=True, blank=True)
    appointment_time = models.ForeignKey(AppointmentTime, on_delete=models.CASCADE, null=True)
    appointment_doctor_time = models.ForeignKey(AppointmentDoctorTime, on_delete=models.CASCADE, null=True)
    doctor_procedure = models.ForeignKey(DoctorProcedures, on_delete=models.SET_NULL, null=True,
                                         blank=True)
    doctor_speciality = models.ForeignKey(DoctorSpecialities, on_delete=models.SET_NULL, null=True,
                                          blank=True)
    is_child = models.BooleanField(default=False, null=True)
    is_visited = models.BooleanField('Посетил', blank=True, null=True)
    note = models.CharField("Примичание", max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.appointment_time.start_time}'


class Comment(TimestampMixin):
    text = models.TextField()
    star = models.PositiveSmallIntegerField('Рейтинг', default=0)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                               related_name="subcomments")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='comments',
                               null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='comments',
                                null=True, blank=True)
    is_responded = models.BooleanField(
        'Ответил',
        default=False,
        blank=True,
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def save(self, *args, **kwargs):
        visited = False
        if not self.parent:
            for appointment in self.patient.appointments.all():
                if appointment.appointment_doctor_time.doctor == self.doctor:
                    visited = True
            if not visited:
                raise exceptions.BadRequest("You can't comment to this doctor")
        super().save(*args, **kwargs)
