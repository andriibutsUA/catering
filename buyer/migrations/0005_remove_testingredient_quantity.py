# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 09:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0004_auto_20170123_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testingredient',
            name='quantity',
        ),
    ]
