# -*- coding: utf-8 -*-
from blog.models import Post
from classytags.core import Tag, Options
from classytags.arguments import Argument
from django.core.urlresolvers import reverse
from django.template import Library

register = Library()

class PostURLTag(Tag):
    name = 'post-url'
    options = Options(
        Argument('post'))

    def render_tag(self, context, post):
        try:
            output = post.get_absolute_url()
        except AttributeError:
            raise Exception("'post-url' template tag argument must be 'Post' "
                            "object.")
        return output
register.tag(PostURLTag)


class PostUpdateURLTag(Tag):
    name = 'post-update-url'
    options = Options(
        Argument('post'))

    def render_tag(self, context, post):
        try:
            output = reverse('blog:update', kwargs={
            'y': post.y,
            'm': post.m,
            'd': post.d,
            'slug': post.slug})
        except AttributeError:
            raise Exception("'post-update-url' template tag argument must be "
                            "'Post' object.")
        return output
register.tag(PostUpdateURLTag)