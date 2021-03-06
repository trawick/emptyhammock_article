# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-05 20:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('cms', '0016_auto_20160608_1535'),
        ('articles', '0016_auto_20171130_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTeaserInRow',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='articles_articleteaserinrow', serialize=False, to='cms.CMSPlugin')),
                ('override_title', models.CharField(blank=True, max_length=80)),
                ('override_subtitle', models.CharField(blank=True, max_length=80)),
                ('override_content', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('override_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'ordering': ('order',),
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='RowOfArticleTeasersPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='articles_rowofarticleteaserspluginmodel', serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='articleteaserinrow',
            name='row',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.RowOfArticleTeasersPluginModel'),
        ),
        migrations.AlterUniqueTogether(
            name='articleteaserinrow',
            unique_together=set([('row', 'order')]),
        ),
    ]
