# Generated by Django 3.2.5 on 2021-07-13 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gmarket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gmarket',
            old_name='band',
            new_name='brand',
        ),
    ]
