# Generated by Django 4.0.5 on 2022-08-11 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0006_doctor_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprocedures',
            name='procedure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_procedures', to='clinics.procedure'),
        ),
    ]