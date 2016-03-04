# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from rawauth.models import Author


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(Author)
    written_in = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
