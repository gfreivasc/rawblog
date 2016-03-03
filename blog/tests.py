# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from model_mommy import mommy
from blog.models import Post
from blog.views import PostCreateView


class PostTest(TestCase):

    def test_case(self):
        pass


class PostCreateViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            'test',
            'te.st@te.st',
            'test'
        )

    def test_form_error_null_post(self):
        response = self.client.post(reverse('blog:new'), {})
        self.assertFormError(response, 'form', 'title', 'This field is required.')
        self.assertFormError(response, 'form', 'content', 'This field is required.')

    def test_assign_logged_in_user(self):
        self.client.login(
            username='test',
            password='test'
        )

        response = self.client.post(reverse('blog:new'), {
            'title':'Hello World!',
            'content':'Its good to be back!'
        })

        post = Post.objects.get(author__pk=self.user.pk)
        self.assertNotEqual(post, None)
        self.assertEqual(post.title, 'Hello World!')

    def test_redirect_correctly(self):
        self.client.login(
            username='test',
            password='test'
        )

        response = self.client.post(reverse('blog:new'), {
            'title':'Hello World!',
            'content':'Its good to be back!'
        })

        self.assertRedirects(response, reverse('blog:posts'))