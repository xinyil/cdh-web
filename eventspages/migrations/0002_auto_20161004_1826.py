# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 22:26
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('eventspages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image'),
        ),
    ]
