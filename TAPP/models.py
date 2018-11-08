# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

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

