# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 21:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_auto_20171025_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substancesurvey',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Country'),
        ),
    ]