from django.db.models import Count, Avg
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from apps.clinics.models import Doctor
from apps.patients.models import Comment


@receiver(post_save, sender=Comment)
def update_score(sender, instance, *args, **kwargs):
    obj = Doctor.objects.get(id=instance.doctor.id)
    doctor = Doctor.objects.filter(id=instance.doctor.id).aggregate(avr_score=Avg('comments__star'))
    obj.score = doctor.get('avr_score')
    obj.save()
