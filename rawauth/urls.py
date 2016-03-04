# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from rawauth.views import author_create_view

app_name = 'rawauth'

urlpatterns = [
    url(r'^login/$', login,
        {'template_name': 'rawauth/login.html'},
        name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^registrate/', author_create_view, name='registration'),
]
