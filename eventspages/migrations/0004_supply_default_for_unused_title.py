# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-31 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventspages', '0003_add_verbose_name_eventslandingpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='title',
            field=models.CharField(default='Events @ CDH', max_length=500),
        ),
    ]
