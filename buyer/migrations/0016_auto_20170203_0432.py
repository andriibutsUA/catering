# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0015_auto_20170203_0426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='ssouce',
            new_name='sauce',
        ),
        migrations.AddField(
            model_name='dish',
            name='sauce_q',
            field=models.PositiveIntegerField(default='10', verbose_name='Количество соуса'),
        ),
    ]
