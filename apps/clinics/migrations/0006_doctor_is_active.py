# Generated by Django 4.0.5 on 2022-08-11 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0005_remove_clinic_image_clinicimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, verbose_name='Активный'),
        ),
    ]