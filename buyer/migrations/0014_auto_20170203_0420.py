# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0013_auto_20170203_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='sss',
            field=models.ManyToManyField(related_name='_dish_sss_+', to='buyer.Dish', verbose_name='Соус'),
        ),
    ]
