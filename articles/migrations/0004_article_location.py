# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20171116_0720'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
