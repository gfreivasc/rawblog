from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
