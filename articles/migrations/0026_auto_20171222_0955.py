# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-22 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_auto_20171212_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlefeedpluginmodel',
            name='flavor',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='articlepluginmodel',
            name='flavor',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='eventfeedpluginmodel',
            name='flavor',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='singlearticleteaserpluginmodel',
            name='flavor',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
