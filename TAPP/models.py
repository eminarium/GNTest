# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    @property
    def full_name(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

    class Meta:
      db_table = "teachers"


class Season(models.Model):
    season_no = models.IntegerField(blank = False)
    season_title = models.CharField(max_length = 50, blank = False)
    season_from_date = models.DateField(blank = False)
    season_to_date = models.DateField(blank = False)
    notes = models.TextField(blank = True)

    class Meta:
        db_table = "seasons"


class Shift(models.Model):
    shift_title = models.CharField(max_length = 50, blank = False)
    shift_from = models.TimeField(blank = False)
    shift_to = models.TimeField(blank = False)
    notes = models.TextField(blank = True)

    class Meta:
        db_table = "shifts"


class Subject(models.Model):
    subject_full_title = models.CharField(max_length = 255, blank = False)
    subject_short_title = models.CharField(max_length = 50, blank = False)
    subject_level = models.IntegerField(blank = False)
    notes = models.TextField(blank = True)

    class Meta:
        db_table = "subjects"

class Topic(models.Model):
    subject = models.ForeignKey(Subject, blank = False)
    topic_title = models.CharField(max_length = 50, blank = False)
    notes = models.TextField(blank = True)

    class Meta:
        db_table = "topics"


class Group(models.Model):
    season = models.ForeignKey(Season, blank = False)
    teacher = models.ForeignKey(Teacher, blank = False)
    shift = models.ForeignKey(Shift, blank = False)
    group_title = models.CharField(max_length = 25, blank = False)
    notes = models.TextField(blank = True)

    class Meta:
        db_table = "groups"

class QuestionBank(models.Model):
    teacher = models.ForeignKey(Teacher, blank = False)
    qb_title = models.CharField(max_length = 50, blank = False)
    date_created = models.DateField(blank = False)
    is_password_protected = models.BooleanField(blank = False)
    qb_password = models.CharField(max_length = 25)
    notes = models.TextField(blank = True)

    class Meta:
        db_table = "question_banks"

