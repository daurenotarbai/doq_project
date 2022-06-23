from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from apps.clinics.models import Doctor
from apps.clinics.serializers import ElasticMainSerializer

@receiver(pre_save, sender=Doctor, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = ElasticMainSerializer(instance)
    obj.save()

@receiver(post_delete, sender=Doctor, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = ElasticMainSerializer(instance)
    obj.delete(ignore=404)