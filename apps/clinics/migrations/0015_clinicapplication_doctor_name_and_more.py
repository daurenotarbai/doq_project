# Generated by Django 4.0.5 on 2022-08-20 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0014_doctorprocedures_child_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicapplication',
            name='doctor_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='clinicapplication',
            name='from_doctor',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='От Доктора'),
        ),
    ]
