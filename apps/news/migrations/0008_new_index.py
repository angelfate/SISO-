# Generated by Django 2.0.6 on 2018-08-25 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_new_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='index',
            field=models.CharField(choices=[('yes', '1'), ('no', '0')], default='no', max_length=6, verbose_name='置顶'),
        ),
    ]