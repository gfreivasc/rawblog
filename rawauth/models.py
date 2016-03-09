# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __unicode__(self):
        return self.get_full_name()