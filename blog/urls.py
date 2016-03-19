# -*- coding: utf-8 -*-
from django.conf.urls import url
from blog.views import post_create_view
from blog.views import post_list_view
from blog.views import post_view
from blog.views import post_update_view

app_name = 'blog'

urlpatterns = [
    url(r'^$', post_list_view, name='posts'),
    url(r'^new/$', post_create_view, name='new'),
    url(r'^(?P<y>[\d]{4})/(?P<m>[\d]{1,2})/(?P<d>[\d]{1,2})/(?P<slug>[\w-]+)'
        r'-(?P<pk>[\d]+)/$', post_view, name='post'),
    url(r'^(?P<y>[\d]{4})/(?P<m>[\d]{1,2})/(?P<d>[\d]{1,2})/(?P<slug>[\w-]+)'
        r'-(?P<pk>[\d]+)/update/$', post_update_view, name='update')
]
