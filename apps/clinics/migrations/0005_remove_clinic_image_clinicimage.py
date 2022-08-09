# Generated by Django 4.0.5 on 2022-08-09 11:42

import apps.clinics.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0004_alter_doctor_operates_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='image',
        ),
        migrations.CreateModel(
            name='ClinicImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=apps.clinics.models.clinic_photo_path, verbose_name='Файл с изображением')),
                ('is_main', models.BooleanField(default=False)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='clinics.clinic')),
            ],
            options={
                'verbose_name': 'Фото клиники',
                'verbose_name_plural': 'Фотографии клиники',
            },
        ),
    ]
