from django.db import transaction
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.utils import IntegrityError
from apps.clinics.models import Doctor, Address, WeekDays, Schedules
from apps.patients.models import Comment


@receiver(post_save, sender=Comment)
def update_score(sender, instance, *args, **kwargs):
    obj = Doctor.objects.get(id=instance.doctor.id)
    doctor = Doctor.objects.filter(id=instance.doctor.id).aggregate(avr_score=Avg('comments__star'))
    obj.score = doctor.get('avr_score')
    obj.save()


@receiver(post_save, sender=Address)
def create_schedules(sender, instance, *args, **kwargs):
    for day in WeekDays.values:
        try:
            with transaction.atomic():
                Schedules.objects.create(day_in_week=day, address=instance)
        except IntegrityError:
            pass
