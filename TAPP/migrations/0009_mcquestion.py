# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-12-14 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TAPP', '0008_auto_20181214_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='McQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField()),
                ('question_txt_content', models.TextField(blank=True)),
                ('question_img_content', models.ImageField(blank=True, upload_to=b'')),
                ('is_multi_response', models.BooleanField()),
                ('points', models.FloatField(blank=True)),
                ('answer_1_txt_content', models.CharField(blank=True, max_length=255)),
                ('answer_1_img_content', models.ImageField(blank=True, upload_to=b'')),
                ('is_answer_1_right', models.BooleanField()),
                ('answer_2_txt_content', models.CharField(blank=True, max_length=255)),
                ('answer_2_img_content', models.ImageField(blank=True, upload_to=b'')),
                ('is_answer_2_right', models.BooleanField()),
                ('answer_3_txt_content', models.CharField(blank=True, max_length=255)),
                ('answer_3_img_content', models.ImageField(blank=True, upload_to=b'')),
                ('is_answer_3_right', models.BooleanField()),
                ('answer_4_txt_content', models.CharField(blank=True, max_length=255)),
                ('answer_4_img_content', models.ImageField(blank=True, upload_to=b'')),
                ('is_answer_4_right', models.BooleanField()),
                ('answer_5_txt_content', models.CharField(blank=True, max_length=255)),
                ('answer_5_img_content', models.ImageField(blank=True, upload_to=b'')),
                ('is_answer_5_right', models.BooleanField()),
                ('answer_6_txt_content', models.CharField(blank=True, max_length=255)),
                ('answer_6_img_content', models.ImageField(blank=True, upload_to=b'')),
                ('is_answer_6_right', models.BooleanField()),
                ('answer_7_txt_content', models.CharField(blank=True, max_length=255)),
                ('answer_7_img_content', models.ImageField(blank=True, upload_to=b'')),
                ('is_answer_7_right', models.BooleanField()),
                ('answer_8_txt_content', models.CharField(blank=True, max_length=255)),
                ('answer_8_img_content', models.ImageField(blank=True, upload_to=b'')),
                ('is_answer_8_right', models.BooleanField()),
                ('notes', models.TextField(blank=True)),
                ('question_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TAPP.QuestionBank')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TAPP.Teacher')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TAPP.Topic')),
            ],
            options={
                'db_table': 'mc_questions',
            },
        ),
    ]