# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffprofiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stafferpage',
            options={'ordering': ['-staffer_data__sortorder']},
        ),
    ]
