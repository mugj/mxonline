# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-06-03 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20190531_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_banne5r',
            field=models.BooleanField(default=False, verbose_name='是否轮播'),
        ),
    ]
