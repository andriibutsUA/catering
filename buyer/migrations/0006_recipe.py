# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_remove_testingredient_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.Dish')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.Ingredient')),
            ],
        ),
    ]
