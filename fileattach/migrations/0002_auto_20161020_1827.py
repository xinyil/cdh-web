# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocktemplate', '0004_auto_20161010_0927'),
        ('fileattach', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileattachment',
            name='generic_template',
        ),
        migrations.AddField(
            model_name='fileattachment',
            name='generic_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stocktemplate.StockLandingPage'),
        ),
    ]