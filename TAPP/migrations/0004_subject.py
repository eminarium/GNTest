# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-08 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAPP', '0003_shift'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_full_title', models.CharField(max_length=255)),
                ('subject_short_title', models.CharField(max_length=50)),
                ('subject_level', models.IntegerField()),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'subjects',
            },
        ),
    ]
