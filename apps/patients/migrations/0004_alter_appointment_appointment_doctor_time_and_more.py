# Generated by Django 4.0.5 on 2022-09-26 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0020_alter_doctor_options'),
        ('patients', '0003_appointment_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_doctor_time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinics.appointmentdoctortime'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinics.appointmenttime'),
        ),
    ]
