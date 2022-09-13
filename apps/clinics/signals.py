from decimal import Decimal

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.utils import IntegrityError
from apps.clinics.models import Doctor, Address, WeekDays, Schedules, DoctorSpecialities, \
    DoctorProcedures, DoctorClinicAddress
from apps.patients.models import Comment


@receiver(post_save, sender=Comment)
def update_score(sender, instance, *args, **kwargs):
    if not instance.parent:
        obj = Doctor.objects.get(id=instance.doctor.id)
        doctor = Doctor.objects.filter(id=instance.doctor.id).aggregate(avr_score=Avg('comments__star'))
        obj.score = doctor.get('avr_score')
        obj.save()


@receiver(post_save, sender=Address)
def create_schedules(sender, instance, *args, **kwargs):
    clinic_doctors_ids = instance.clinic.doctors.all().values_list('id', flat=True)
    try:
        doctor_addresses = []
        for id in clinic_doctors_ids:
            doctor_address = DoctorClinicAddress(doctor_id=id, address=instance)
            doctor_addresses.append(doctor_address)
        with transaction.atomic():
            DoctorClinicAddress.objects.bulk_create(doctor_addresses)
    except Exception as e:
        print("R",e)
    try:
        with transaction.atomic():
            for pk in clinic_doctors_ids:
                obj = DoctorProcedures.objects.get(doctor_id=pk)
                obj.pk = None
                obj.address = instance
                obj.save()
    except (IntegrityError, ObjectDoesNotExist) as e:
        print("RR", e)
    try:
        with transaction.atomic():
            for id in clinic_doctors_ids:
                obj = DoctorSpecialities.objects.get(doctor_id=id)
                obj.pk = None
                obj.address = instance
                obj.save()

    except (IntegrityError, ObjectDoesNotExist) as e:
        print("RRR", e)

    for day in WeekDays.values:
        try:
            if instance.is_24_hours:
                with transaction.atomic():
                    Schedules.objects.update_or_create(day_in_week=day,
                                                       address=instance,
                                                       defaults={
                                                           'start_day': "00:00:00",
                                                           'end_day': "23:59:59",
                                                       })
            else:
                with transaction.atomic():
                    Schedules.objects.create(day_in_week=day, address=instance)
        except IntegrityError:
            pass


@receiver(post_save, sender=DoctorSpecialities)
def update_speciality_new_price(sender, instance, *args, **kwargs):
    if instance.discount != 0:
        new_price = instance.price - Decimal(instance.discount)
        DoctorSpecialities.objects.filter(id=instance.id).update(new_price=new_price)
    else:
        DoctorSpecialities.objects.filter(id=instance.id).update(new_price=0.00)


@receiver(post_save, sender=DoctorProcedures)
def update_procedure_new_price(sender, instance, *args, **kwargs):
    if instance.discount != 0:
        new_price = instance.price - Decimal(instance.discount)
        DoctorProcedures.objects.filter(id=instance.id).update(new_price=new_price)
    else:
        DoctorProcedures.objects.filter(id=instance.id).update(new_price=0.00)


@receiver(post_save, sender=Doctor)
def update_consultation_new_price(sender, instance, *args, **kwargs):
    if instance.discount_consultation_fee != 0:
        new_price = instance.consultation_fee - Decimal(instance.discount_consultation_fee)
        Doctor.objects.filter(id=instance.id).update(new_price=new_price)
    else:
        Doctor.objects.filter(id=instance.id).update(new_price=0.00)