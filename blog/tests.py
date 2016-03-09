# -*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
from rawauth.models import Author
from blog.models import Post
from model_mommy import mommy


class PostTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create_user(
            'test',
            'te.st@te.st',
            'test')
        self.author.save()
        self.post = mommy.make(Post, author=self.author)
        self.post.save()

    def test_post_created_successfully(self):
        self.assertEqual(len(Post.objects.filter(author=self.author)), 1)

    def test_post_last_edited(self):
        self.post.content = 'A whole new thing'
        self.post.save()
        self.assertNotEqual(self.post.last_edited, self.post.written_in)


class PostCreateViewTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create_user(
            'test',
            'te.st@te.st',
            'test')

    def test_form_error_null_post(self):
        self.client.login(username='test', password='test')
        response = self.client.post(reverse('blog:new'), {})

        self.assertFormError(response, 'form', 'title',
                             'This field is required.')
        self.assertFormError(response, 'form', 'content',
                             'This field is required.')

    def test_assign_logged_in_author(self):
        self.client.login(username='test', password='test')

        self.client.post(reverse('blog:new'), {
            'title': 'Hello World!',
            'content': 'Its good to be back!'})

        post = Post.objects.get(author__pk=self.author.pk)
        self.assertNotEqual(post, None)
        self.assertEqual(post.title, 'Hello World!')

    def test_redirect_correctly(self):
        self.client.login(username='test', password='test')

        response = self.client.post(reverse('blog:new'), {
            'title': 'Hello World!',
            'content': 'Its good to be back!'})

        self.assertRedirects(response, reverse('blog:posts'))

    def test_create_post_view_requires_login_and_redirects(self):
        response = self.client.post(reverse('blog:new'))

        self.assertRedirects(
            response,
            reverse('rawauth:login')+'?next='+reverse('blog:new'),
            status_code=302,
            target_status_code=200)
