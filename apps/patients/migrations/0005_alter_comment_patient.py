# Generated by Django 4.0.5 on 2022-08-19 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_appointment_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='patients.patient'),
        ),
    ]
