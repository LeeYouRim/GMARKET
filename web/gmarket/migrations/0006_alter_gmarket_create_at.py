# Generated by Django 3.2.5 on 2021-07-13 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmarket', '0005_alter_gmarket_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmarket',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 13, 18, 19, 19, 497331)),
        ),
    ]
