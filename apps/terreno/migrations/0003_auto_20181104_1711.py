# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-04 22:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terreno', '0002_siembra_robot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siembra',
            name='donacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='financiacion.Donacion'),
        ),
    ]
