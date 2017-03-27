# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0019_auto_20170213_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('1', 'Холодные закуски'), ('2', 'Закуски'), ('3', 'Горячие закуски'), ('4', 'Вторые блюда'), ('5', 'Гарниры'), ('6', 'Десерты'), ('7', 'Барбекю'), ('8', 'Напитки'), ('9', 'Соусы'), ('10', 'Спорт'), ('11', 'Канапе'), ('12', 'Салаты'), ('13', 'Намазки')], default='2', max_length=2, verbose_name='Категория'),
        ),
    ]