# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0018_auto_20170212_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('1', 'Холодные закуски'), ('2', 'Закуски'), ('3', 'Горячие закуски'), ('4', 'Вторые блюда'), ('5', 'Гарниры'), ('6', 'Десерты'), ('7', 'Барбекю'), ('8', 'Напитки'), ('9', 'Соусы'), ('10', 'Спорт'), ('11', 'Канапе'), ('12', 'Салаты')], default='2', max_length=2, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='category',
            field=models.CharField(choices=[('1', 'Грибы'), ('2', 'Колбасные изделия'), ('3', 'Крупы и каши'), ('4', 'Масла и жиры'), ('5', 'Яйца'), ('6', 'Ягоды'), ('7', 'Фрукты'), ('8', 'Молочные продукты'), ('9', 'Мука и макаронные изделия'), ('10', 'Орехи и сухофрукты'), ('11', 'Мясопродукты'), ('12', 'Овощи и зелень'), ('13', 'Рыба и морепродукты'), ('14', 'Сыры и творог'), ('15', 'Хлебобулочные изделия'), ('16', 'Напитки алкогольные'), ('17', 'Напитки безалкогольные'), ('18', 'Соки и компоты'), ('19', 'Приправы и специи'), ('20', 'Разное')], default='1', max_length=2, verbose_name='Категория'),
        ),
    ]
