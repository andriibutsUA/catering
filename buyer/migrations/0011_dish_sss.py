# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0010_auto_20170203_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='sss',
            field=models.ManyToManyField(related_name='_dish_sss_+', to='buyer.Dish', verbose_name='Соус'),
        ),
    ]
