# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0011_auto_20171025_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='substancesurvey',
            name='color',
        ),
        migrations.AddField(
            model_name='substancesurvey',
            name='color',
            field=models.ManyToManyField(blank=True, to='survey.Color'),
        ),
    ]
