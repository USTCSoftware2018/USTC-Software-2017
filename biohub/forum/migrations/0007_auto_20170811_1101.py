# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 10:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0006_auto_20170811_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='up_vote_num',
        ),
        migrations.RemoveField(
            model_name='post',
            name='up_vote_users',
        ),
        migrations.AddField(
            model_name='experience',
            name='up_vote_num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='experience',
            name='up_vote_users',
            field=models.ManyToManyField(related_name='experiences_voted', to=settings.AUTH_USER_MODEL),
        ),
    ]
