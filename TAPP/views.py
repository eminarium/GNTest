# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Create your views here.

class index(TemplateView):
    template_name = "index.html"
