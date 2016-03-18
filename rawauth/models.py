# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __unicode__(self):
        return self.get_full_name()


class Commentator(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    author = models.ForeignKey(Author)

    class Meta:
        verbose_name = "Commentator"
        verbose_name_plural = "Commentators"

    def __unicode__(self):
        if self.author is not None:
            return unicode(self.author)
        else:
            return u'{0} - {1}'.format(self.name, self.email)
