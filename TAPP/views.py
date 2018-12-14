# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
from .models import *

# Create your views here.

def seasons(request):
    seasons = Season.objects.all()

    return render(request, "seasons.html", {'seasons':seasons})

def subjects(request):
    subjects = Subject.objects.all()

    return render(request, "subjects.html", {'subjects':subjects})

def shifts(request):
    shifts = Shift.objects.all()

    return render(request, "shifts.html", {'shifts':shifts, 'counter':0})

def topics(request):
    topics = Topic.objects.all()

    return render(request, "topics.html", {'topics':topics, 'counter':0})

def groups(request):
    groups = Group.objects.all()

    return render(request, "groups.html", {'groups':groups, 'counter':0})

def question_banks(request):
    question_banks = QuestionBank.objects.all()

    return render(request, "question_banks.html", {'question_banks':question_banks, 'counter':0})
