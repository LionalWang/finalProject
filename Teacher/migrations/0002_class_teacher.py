# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.CharField(default='null', max_length=256, verbose_name='Teacher'),
        ),
    ]
