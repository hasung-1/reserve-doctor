# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-02 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_auto_20180302_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='sidogungu',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital.Sido'),
            preserve_default=False,
        ),
    ]
