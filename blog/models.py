# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from rawauth.models import Author
from rawauth.models import Commentator


class BlogModel(models.Model):
    content = models.TextField()
    written_in = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(BlogModel):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return u'{0} - {1}'.format(self.title, self.author)

    @property
    def d(self):
        return self.written_in.date().day

    @property
    def m(self):
        return self.written_in.date().month

    @property
    def y(self):
        return self.written_in.date().year

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={
            'y': self.y,
            'm': self.m,
            'd': self.d,
            'slug': self.slug})


class Comment(BlogModel):
    post = models.ForeignKey(Post)
    commentator = models.ForeignKey(Commentator)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __unicode__(self):
        return u'{0} on {1}'.format(self.commentator, self.post.title)
