# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 22:33
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projectpages', '0004_auto_20161004_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='override_image',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='project_image',
            field=mezzanine.core.fields.FileField(max_length=255),
        ),
    ]