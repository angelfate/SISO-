# Generated by Django 2.0.6 on 2018-08-22 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='历届干部')),
                ('student', models.CharField(max_length=20, verbose_name='姓名')),
                ('image', models.ImageField(upload_to='cardes/%Y%m', verbose_name='头像')),
                ('grade', models.IntegerField(verbose_name='年级')),
                ('job', models.CharField(max_length=20, verbose_name='担任职务')),
                ('declaration', models.CharField(max_length=20, verbose_name='个人宣言')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '历届干部',
                'verbose_name_plural': '历届干部',
            },
        ),
    ]