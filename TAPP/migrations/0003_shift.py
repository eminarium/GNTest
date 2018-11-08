# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-08 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAPP', '0002_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_title', models.CharField(max_length=50)),
                ('shift_from', models.TimeField()),
                ('shift_to', models.TimeField()),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'shifts',
            },
        ),
    ]
