# Generated by Django 3.1.7 on 2021-03-07 19:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bp', '0012_auto_20210307_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 7, 22, 31, 17, 92835)),
        ),
    ]
