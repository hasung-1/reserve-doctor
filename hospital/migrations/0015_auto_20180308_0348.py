# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_auto_20180306_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='addr',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='tel',
            field=models.CharField(max_length=14),
        ),
    ]
