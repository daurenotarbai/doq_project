# Generated by Django 4.0.5 on 2022-08-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='achievements',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Достижении'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='category',
            field=models.CharField(blank=True, choices=[('FIRST', 'Первая категория'), ('SECOND', 'Вторая категория'), ('HIGHER', 'Высшая категория')], max_length=20, null=True, verbose_name='Категория'),
        ),
    ]
