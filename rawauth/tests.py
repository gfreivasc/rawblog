from django.test import TestCase
from django.core.urlresolvers import reverse
from rawauth.models import Author


class AuthorTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create_user('Meme', 'meme@dot.com',
                                                 'tester')
        self.author.save()

    def test_author_created_successfully(self):
        self.assertNotEqual(len(Author.objects.all()), 0)

    def test_author_logs_in(self):
        self.client.login(username='Meme', password='tester')
        self.assertEqual(int(self.client.session['_auth_user_id']),
                         self.author.pk)


class AuthorCreateViewTest(TestCase):

    def setUp(self):
        self.post_data = {
            'username': 'test',
            'email': 'te.st@te.st',
            'first_name': 'Test',
            'last_name': 'Case',
            'password1': 'test123',
            'password2': 'test123',
        }

    def test_author_logs_in_after_creation(self):
        response = self.client.post(reverse('rawauth:registration'),
                                    self.post_data)
        self.assertEqual(response.status_code, 302)

        self.assertIn('_auth_user_id', self.client.session)

    def test_fails_passwords_dont_match(self):
        post_data = self.post_data
        post_data['password2'] = 'unmatching'

        response = self.client.post(reverse('rawauth:registration'),
                                    self.post_data)
        self.assertContains(response, "Passwords don&#39;t match!")

    def test_author_registration_redirects_to_next(self):
        response = self.client.post(
            reverse('rawauth:registration')+'?next='+reverse('blog:new'),
            self.post_data
        )

        self.assertRedirects(response, reverse('blog:new'),
                             status_code=302, target_status_code=200)
