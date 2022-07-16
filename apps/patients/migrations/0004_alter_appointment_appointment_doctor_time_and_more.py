# Generated by Django 4.0.5 on 2022-07-16 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0004_clinic_image_delete_clinicphoto'),
        ('patients', '0003_remove_appointment_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_doctor_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinics.appointmentdoctortime'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinics.appointmenttime'),
        ),
    ]
