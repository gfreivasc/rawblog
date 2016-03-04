from django.test import TestCase
from django.core.urlresolvers import reverse


class AuthorTest(TestCase):

    def test_case(self):
        pass


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

    def test_user_logs_in_after_creation(self):
        response = self.client.post(reverse('rawauth:registration'),
                                    self.post_data)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('blog:new'))
        self.assertEqual(response.status_code, 200)

    def test_fails_passwords_dont_match(self):
        post_data = self.post_data
        post_data['password2'] = 'unmatching'

        response = self.client.post(reverse('rawauth:registration'),
                                    self.post_data)
        self.assertContains(response, "Passwords don&#39;t match!")
