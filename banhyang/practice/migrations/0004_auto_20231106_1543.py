# Generated by Django 3.0.4 on 2023-11-06 06:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_songdata_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songdata',
            name='priority',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
    ]
