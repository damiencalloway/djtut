#! /usr/bin/env python

from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('', url(r'^S', views.index, name='index')
)
