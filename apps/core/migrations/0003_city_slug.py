# Generated by Django 4.0.5 on 2022-09-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_city_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.CharField(default='', max_length=50, verbose_name='slug'),
        ),
    ]
