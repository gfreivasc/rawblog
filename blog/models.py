# -*- coding: utf-8 -*-
from autoslug import AutoSlugField
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
    slug = AutoSlugField(populate_from='title', unique_with=['d', 'm', 'y'],
                         null=True, blank=True)
    d = models.PositiveIntegerField(default=1, null=True, blank=True)
    m = models.PositiveIntegerField(default=1, null=True, blank=True)
    y = models.PositiveIntegerField(default=2016, null=True, blank=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return u'{0} - {1}'.format(self.title, self.author)

    def set_written_in_data(self):
        self.d = self.written_in.date().day
        self.m = self.written_in.date().month
        self.y = self.written_in.date().year

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={
            'y': self.y,
            'm': self.m,
            'd': self.d,
            'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            super(Post, self).save(*args, **kwargs)
            self.set_written_in_data()
        super(Post, self).save(*args, **kwargs)


class Comment(BlogModel):
    post = models.ForeignKey(Post)
    commentator = models.ForeignKey(Commentator)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __unicode__(self):
        return u'{0} on {1}'.format(self.commentator, self.post.title)
