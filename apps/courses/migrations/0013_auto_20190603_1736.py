# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-06-03 17:36
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20190603_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情'),
        ),
    ]
