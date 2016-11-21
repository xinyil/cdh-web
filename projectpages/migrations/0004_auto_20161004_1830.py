# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 22:30
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projectpages', '0003_project_project_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='override_image',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='project_image',
            field=mezzanine.core.fields.FileField(max_length=255, verbose_name='Image'),
        ),
    ]