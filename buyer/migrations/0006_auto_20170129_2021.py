# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_auto_20170129_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buyer.Ingredient', verbose_name='Ингредиент'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Брутто'),
        ),
    ]