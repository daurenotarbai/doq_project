# Generated by Django 4.0.5 on 2022-09-19 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0016_appointmenttime_code'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointmenttime',
            unique_together={('start_time', 'code')},
        ),
    ]
