# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.edit import CreateView
from blog.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

post_create_view = PostCreateView.as_view()