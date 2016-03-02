# -*- coding: utf-8 -*-

from django.conf.urls import url
from blog.views import post_create_view

urlpatterns = [
    url(r'^new/', post_create_view),
]