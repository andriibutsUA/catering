# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0007_auto_20170123_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='privet',
            field=models.CharField(default='Здоров пацаны', max_length=250, verbose_name='Приветики'),
        ),
    ]
