# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 20:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('date', models.DateField(default=datetime.datetime(2017, 6, 11, 20, 27, 43, 247057, tzinfo=utc))),
            ],
        ),
    ]
