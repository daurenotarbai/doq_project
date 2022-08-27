# Generated by Django 4.0.5 on 2022-08-27 12:45

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0006_alter_clinicapplication_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprocedures',
            name='new_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
        migrations.AddField(
            model_name='doctorspecialities',
            name='new_price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
    ]