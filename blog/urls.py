# -*- coding: utf-8 -*-
from django.conf.urls import url
from blog.views import post_list_view, post_create_view

app_name = 'blog'

urlpatterns = [
    url(r'^$', post_list_view, name='posts'),
    url(r'^new/$', post_create_view, name='new'),
]
