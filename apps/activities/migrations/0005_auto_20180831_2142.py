# Generated by Django 2.0.6 on 2018-08-31 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_auto_20180831_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadres',
            old_name='satrt_time',
            new_name='start_time',
        ),
    ]
