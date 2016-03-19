# -*- coding: utf-8 -*-
from django.conf.urls import url
from blog.views import post_list_view, post_create_view, post_view

app_name = 'blog'

urlpatterns = [
    url(r'^$', post_list_view, name='posts'),
    url(r'^new/$', post_create_view, name='new'),
    url(r'^(?P<y>[\d]{4})/(?P<m>[\d]{1,2})/(?P<d>[\d]{1,2})/(?P<slug>[\w-]+)'
        '-(?P<pk>[\d]+)/$',
        post_view, name='post')
]
