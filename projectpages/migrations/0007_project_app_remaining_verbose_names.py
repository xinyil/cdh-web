# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-30 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectpages', '0006_add_verbose_project_member'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectrole',
            options={'verbose_name': 'Project Role'},
        ),
        migrations.AlterModelOptions(
            name='projectslandingpage',
            options={'ordering': ('_order',), 'verbose_name': 'Project List'},
        ),
    ]