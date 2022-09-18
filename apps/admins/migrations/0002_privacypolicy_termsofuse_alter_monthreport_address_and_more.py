# Generated by Django 4.0.5 on 2022-09-17 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0016_appointmenttime_code'),
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Политика конфиденциальности')),
                ('file', models.FileField(max_length=254, upload_to='privacy-policy')),
            ],
            options={
                'verbose_name': 'Политика конфиденциальности',
                'verbose_name_plural': 'Политика конфиденциальности',
            },
        ),
        migrations.CreateModel(
            name='TermsOfUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Пользовательское соглашение')),
                ('file', models.FileField(max_length=254, upload_to='terms-of-use')),
            ],
            options={
                'verbose_name': 'Пользовательское соглашение',
                'verbose_name_plural': 'Пользовательские соглашении',
            },
        ),
        migrations.AlterField(
            model_name='monthreport',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinics.address', verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='monthreport',
            name='status',
            field=models.CharField(choices=[('DONE', 'сдана'), ('PAID', 'оплачено'), ('UNPAID', 'сверка')], default='UNPAID', max_length=12, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='monthreport',
            name='total_appointments',
            field=models.PositiveIntegerField(default=0, verbose_name='Всего заявок'),
        ),
        migrations.AlterField(
            model_name='monthreport',
            name='verified',
            field=models.PositiveIntegerField(default=0, verbose_name='Сверенных'),
        ),
    ]