# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 13:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='actor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notice',
            name='target_id',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='notice',
            name='target_slug',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='notice',
            name='target_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
