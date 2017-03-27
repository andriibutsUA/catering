# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0009_auto_20170129_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='souce',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='souce_q',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='first_supplier',
            field=models.CharField(default='Novus', max_length=200, verbose_name='Производитель 1'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='second_supplier',
            field=models.CharField(default='Novus', max_length=200, verbose_name='Производитель 2'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='third_supplier',
            field=models.CharField(default='Novus', max_length=200, verbose_name='Производитель 3'),
        ),
    ]