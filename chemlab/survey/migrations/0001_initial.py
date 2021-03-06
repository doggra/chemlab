# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apperance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SubstanceSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('date', models.CharField(blank=True, max_length=255)),
                ('price', models.CharField(blank=True, max_length=255)),
                ('alias', models.CharField(blank=True, max_length=255)),
                ('substance', models.CharField(max_length=255)),
                ('color', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='media/substances')),
                ('observations', models.TextField(blank=True)),
                ('user_code', models.CharField(blank=True, max_length=255)),
                ('apperance', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Apperance')),
                ('city', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='survey.City')),
                ('country', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Country')),
                ('kind', models.ManyToManyField(blank=True, to='survey.Kind')),
                ('origin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Origin')),
                ('source', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Source')),
            ],
        ),
        migrations.CreateModel(
            name='TestMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='substancesurvey',
            name='test_methods',
            field=models.ManyToManyField(blank=True, to='survey.TestMethod'),
        ),
    ]
