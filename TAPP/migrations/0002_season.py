# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-08 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_no', models.IntegerField()),
                ('season_title', models.CharField(max_length=50)),
                ('season_from_date', models.DateField()),
                ('season_to_date', models.DateField()),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'seasons',
            },
        ),
    ]
