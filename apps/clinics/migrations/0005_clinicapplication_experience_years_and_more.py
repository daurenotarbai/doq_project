# Generated by Django 4.0.5 on 2022-08-27 08:00

import apps.clinics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0004_alter_appointmentdoctortime_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicapplication',
            name='experience_years',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Опыт работы'),
        ),
        migrations.AddField(
            model_name='clinicapplication',
            name='image',
            field=models.ImageField(blank=True, upload_to=apps.clinics.models.doctor_application_photo_path, verbose_name='Лого клиники'),
        ),
        migrations.AddField(
            model_name='clinicapplication',
            name='institution',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Учебное заведение'),
        ),
        migrations.AddField(
            model_name='clinicapplication',
            name='speciality',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Специальность'),
        ),
    ]
