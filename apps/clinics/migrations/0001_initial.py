# Generated by Django 4.0.5 on 2022-07-28 03:48

import apps.clinics.models
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Время начало приема')),
            ],
            options={
                'verbose_name': 'Интервал времени',
                'verbose_name_plural': 'Интервалы времени',
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время создания')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Время последнего изменения')),
                ('phone', models.CharField(default='', max_length=20, verbose_name='Мобильный телефон')),
                ('work_phone', models.CharField(default='', max_length=20, verbose_name='Рабочий телефон')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Название клиники')),
                ('description', models.TextField(blank=True, default='', help_text='Подробное описание', verbose_name='Описание')),
                ('logo', models.ImageField(blank=True, upload_to=apps.clinics.models.clinic_photo_path, verbose_name='Лого клиники')),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.clinics.models.clinic_photo_path, verbose_name='Файл с изображением')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='Актив')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clinic', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Клиника',
                'verbose_name_plural': 'Клиники',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время создания')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Время последнего изменения')),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(default='', max_length=255, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, default='', max_length=255, verbose_name='Отчество')),
                ('description', models.TextField(blank=True, default='', help_text='Подробное описание', verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=apps.clinics.models.specialist_photo_path, verbose_name='Фото специалиста')),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'Мужской'), ('FEMALE', 'Женский')], max_length=10, null=True, verbose_name='Пол')),
                ('experience_years', models.PositiveSmallIntegerField(default=1, null=True, verbose_name='Опыт работы')),
                ('consultation_fee', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10, verbose_name='Цена за прием')),
                ('score', models.FloatField(default=0.0, verbose_name='Рейтинг')),
                ('for_child', models.BooleanField(blank=True, default=True, verbose_name='Детский')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='clinics.clinic', verbose_name='Клиника')),
            ],
            options={
                'verbose_name': 'Доктор',
                'verbose_name_plural': 'Докторы',
            },
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название специальности')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255, verbose_name='Название процедуры')),
                ('is_specialty', models.BooleanField(blank=True, default=True, verbose_name='По специальности')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subprocedures', to='clinics.procedure')),
            ],
            options={
                'verbose_name': 'Процедура',
                'verbose_name_plural': 'Процедуры',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='DoctorProcedures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_procedures', to='clinics.doctor')),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinics.procedure')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='procedures',
            field=models.ManyToManyField(related_name='doctors', through='clinics.DoctorProcedures', to='clinics.procedure', verbose_name='Процедуры'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialities',
            field=models.ManyToManyField(related_name='doctors', to='clinics.speciality', verbose_name='Специальности'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=255, null=True, verbose_name='Город')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адресс')),
                ('is_24_hours', models.BooleanField(blank=True, default=False, verbose_name='Круглосуточно')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='clinics.clinic')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_in_week', models.CharField(blank=True, choices=[('MONDAY', 'Понедельник'), ('TUESDAY', 'Вторник'), ('WEDNESDAY', 'Среда'), ('THURSDAY', 'Четверг'), ('FRIDAY', 'Пятница'), ('SATURDAY', 'Суббота'), ('SUNDAY', 'Воскресенье')], max_length=255, null=True, verbose_name='День недели')),
                ('start_day', models.TimeField(null=True)),
                ('end_day', models.TimeField(null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='clinics.address')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписании',
                'unique_together': {('day_in_week', 'address')},
            },
        ),
        migrations.CreateModel(
            name='AppointmentDoctorTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('clinic_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appoint_times', to='clinics.address', verbose_name='Адрес клиники')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appoint_times', to='clinics.doctor', verbose_name='Доктор')),
                ('times', models.ManyToManyField(blank=True, to='clinics.appointmenttime', verbose_name='Времени на прием')),
            ],
            options={
                'verbose_name': 'Времени на прием',
                'verbose_name_plural': 'Времени на прием',
                'unique_together': {('doctor', 'date')},
            },
        ),
    ]
