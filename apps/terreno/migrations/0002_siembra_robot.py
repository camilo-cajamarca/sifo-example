# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-11-04 21:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_auto_20181104_1637'),
        ('terreno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siembra',
            name='robot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.Robot'),
        ),
    ]
