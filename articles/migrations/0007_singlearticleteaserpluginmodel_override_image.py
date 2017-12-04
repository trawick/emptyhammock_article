# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 17:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('articles', '0006_singlearticleteaserpluginmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlearticleteaserpluginmodel',
            name='override_image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL),
        ),
    ]
