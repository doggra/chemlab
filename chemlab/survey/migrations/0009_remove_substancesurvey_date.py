# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 20:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_auto_20171025_0208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='substancesurvey',
            name='date',
        ),
    ]
