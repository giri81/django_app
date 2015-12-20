# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^compile/$', 'compile', name='compile'),
)
