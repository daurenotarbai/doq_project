# Generated by Django 4.0.5 on 2022-08-17 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinics', '0012_alter_address_latitude_alter_address_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время создания')),
                ('changed_at', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Время последнего изменения')),
                ('month', models.DateField(verbose_name='Месяц')),
                ('verified', models.PositiveIntegerField(default=0)),
                ('total_appointments', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('DONE', 'сдана'), ('PAID', 'оплачено'), ('UNPAID', 'сверка')], max_length=12, verbose_name='Номер телефона')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinics.address')),
            ],
            options={
                'verbose_name': 'Сверка',
                'verbose_name_plural': 'Сверка',
                'unique_together': {('month', 'address')},
            },
        ),
    ]