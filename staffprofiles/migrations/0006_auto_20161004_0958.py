# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 13:58
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('staffprofiles', '0005_auto_20161003_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffer',
            name='photo',
            field=mezzanine.core.fields.FileField(max_length=255, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='staffer',
            name='profile_photo',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Image'),
        ),
    ]
