# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180305_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital_user',
            name='tel',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]