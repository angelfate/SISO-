# Generated by Django 2.0.6 on 2018-08-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadres', '0002_cadres_professions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadres',
            name='professions',
            field=models.CharField(default='计算机信息管理', max_length=20, verbose_name='专业'),
        ),
    ]
