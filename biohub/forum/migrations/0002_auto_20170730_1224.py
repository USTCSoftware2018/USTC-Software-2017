# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 11:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='pub_time',
            field=models.DateField(default=datetime.date.today, verbose_name='publish time'),
        ),
    ]