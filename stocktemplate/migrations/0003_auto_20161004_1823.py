# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 22:23
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stocktemplate', '0002_auto_20160923_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklandingpage',
            name='image',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image'),
        ),
    ]
