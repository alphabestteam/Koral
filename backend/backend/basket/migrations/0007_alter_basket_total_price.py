# Generated by Django 4.2.6 on 2023-12-19 17:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_basket_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='total_price',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
