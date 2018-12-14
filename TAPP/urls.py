from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^seasons/$', views.seasons, name='seasons'),
    url(r'^subjects/$', views.subjects, name='subjects'),
    url(r'^shifts/$', views.shifts, name='shifts'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^question_banks/$', views.question_banks, name='question_banks'),
]