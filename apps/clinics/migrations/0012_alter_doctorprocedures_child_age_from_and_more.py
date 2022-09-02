# Generated by Django 4.0.5 on 2022-08-30 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinics', '0011_alter_doctorprocedures_child_age_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprocedures',
            name='child_age_from',
            field=models.CharField(blank=True, choices=[('0 мес.', '0 мес.'), ('1 мес.', '1 мес.'), ('2 мес.', '2 мес.'), ('3 мес.', '3 мес.'), ('4 мес.', '4 мес.'), ('5 мес.', '5 мес.'), ('6 мес.', '6 мес.'), ('7 мес.', '7 мес.'), ('8 мес.', '8 мес.'), ('9 мес.', '9 мес.'), ('10 мес.', '10 мес.'), ('11 мес.', '11 мес.'), ('1 год', '1 год'), ('2 года', '2 года'), ('3 года', '3 года'), ('4 года', '4 года'), ('5 лет', '5 лет'), ('6 лет', '6 лет'), ('7 лет', '7 лет'), ('8 лет', '8 лет'), ('9 лет', '9 лет'), ('10 лет', '10 лет'), ('11 лет', '11 лет'), ('12 лет', '12 лет'), ('13 лет', '13 лет'), ('14 лет', '14 лет'), ('15 лет', '15 лет'), ('16 лет', '16 лет'), ('17 лет', '17 лет'), ('18 лет', '18 лет')], max_length=255, null=True, verbose_name='Возраст детей от'),
        ),
        migrations.AlterField(
            model_name='doctorprocedures',
            name='child_age_to',
            field=models.CharField(blank=True, choices=[('0 мес.', '0 мес.'), ('1 мес.', '1 мес.'), ('2 мес.', '2 мес.'), ('3 мес.', '3 мес.'), ('4 мес.', '4 мес.'), ('5 мес.', '5 мес.'), ('6 мес.', '6 мес.'), ('7 мес.', '7 мес.'), ('8 мес.', '8 мес.'), ('9 мес.', '9 мес.'), ('10 мес.', '10 мес.'), ('11 мес.', '11 мес.'), ('1 год', '1 год'), ('2 года', '2 года'), ('3 года', '3 года'), ('4 года', '4 года'), ('5 лет', '5 лет'), ('6 лет', '6 лет'), ('7 лет', '7 лет'), ('8 лет', '8 лет'), ('9 лет', '9 лет'), ('10 лет', '10 лет'), ('11 лет', '11 лет'), ('12 лет', '12 лет'), ('13 лет', '13 лет'), ('14 лет', '14 лет'), ('15 лет', '15 лет'), ('16 лет', '16 лет'), ('17 лет', '17 лет'), ('18 лет', '18 лет')], max_length=255, null=True, verbose_name='Возраст детей до'),
        ),
        migrations.AlterField(
            model_name='doctorspecialities',
            name='child_age_from',
            field=models.CharField(blank=True, choices=[('0 мес.', '0 мес.'), ('1 мес.', '1 мес.'), ('2 мес.', '2 мес.'), ('3 мес.', '3 мес.'), ('4 мес.', '4 мес.'), ('5 мес.', '5 мес.'), ('6 мес.', '6 мес.'), ('7 мес.', '7 мес.'), ('8 мес.', '8 мес.'), ('9 мес.', '9 мес.'), ('10 мес.', '10 мес.'), ('11 мес.', '11 мес.'), ('1 год', '1 год'), ('2 года', '2 года'), ('3 года', '3 года'), ('4 года', '4 года'), ('5 лет', '5 лет'), ('6 лет', '6 лет'), ('7 лет', '7 лет'), ('8 лет', '8 лет'), ('9 лет', '9 лет'), ('10 лет', '10 лет'), ('11 лет', '11 лет'), ('12 лет', '12 лет'), ('13 лет', '13 лет'), ('14 лет', '14 лет'), ('15 лет', '15 лет'), ('16 лет', '16 лет'), ('17 лет', '17 лет'), ('18 лет', '18 лет')], max_length=255, null=True, verbose_name='Возраст детей от'),
        ),
        migrations.AlterField(
            model_name='doctorspecialities',
            name='child_age_to',
            field=models.CharField(blank=True, choices=[('0 мес.', '0 мес.'), ('1 мес.', '1 мес.'), ('2 мес.', '2 мес.'), ('3 мес.', '3 мес.'), ('4 мес.', '4 мес.'), ('5 мес.', '5 мес.'), ('6 мес.', '6 мес.'), ('7 мес.', '7 мес.'), ('8 мес.', '8 мес.'), ('9 мес.', '9 мес.'), ('10 мес.', '10 мес.'), ('11 мес.', '11 мес.'), ('1 год', '1 год'), ('2 года', '2 года'), ('3 года', '3 года'), ('4 года', '4 года'), ('5 лет', '5 лет'), ('6 лет', '6 лет'), ('7 лет', '7 лет'), ('8 лет', '8 лет'), ('9 лет', '9 лет'), ('10 лет', '10 лет'), ('11 лет', '11 лет'), ('12 лет', '12 лет'), ('13 лет', '13 лет'), ('14 лет', '14 лет'), ('15 лет', '15 лет'), ('16 лет', '16 лет'), ('17 лет', '17 лет'), ('18 лет', '18 лет')], max_length=255, null=True, verbose_name='Возраст детей до'),
        ),
    ]