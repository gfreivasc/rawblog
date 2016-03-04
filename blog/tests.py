# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from rawauth.models import Author
from blog.models import Post


class PostTest(TestCase):

    def test_case(self):
        pass


class PostCreateViewTest(TestCase):

    def setUp(self):
        self.user = Author.objects.create_user(
            'test',
            'te.st@te.st',
            'test'
        )

    def test_form_error_null_post(self):
        self.client.login(
            username='test',
            password='test'
        )
        response = self.client.post(reverse('blog:new'), {})

        self.assertFormError(response, 'form', 'title',
                             'This field is required.')
        self.assertFormError(response, 'form', 'content',
                             'This field is required.')

    def test_assign_logged_in_user(self):
        self.client.login(
            username='test',
            password='test'
        )

        self.client.post(reverse('blog:new'), {
            'title': 'Hello World!',
            'content': 'Its good to be back!'
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
            'title': 'Hello World!',
            'content': 'Its good to be back!'
        })

        self.assertRedirects(response, reverse('blog:posts'))

    def test_create_post_view_requires_login_and_redirects(self):
        response = self.client.post(reverse('blog:new'))

        self.assertRedirects(
            response,
            reverse('rawauth:login')+'?next='+reverse('blog:new'),
            status_code=302,
            target_status_code=200)
