from django.test import TestCase
from django.core.urlresolvers import reverse


class AuthorTest(TestCase):

    def test_case(self):
        pass


class AuthorCreateViewTest(TestCase):

    def test_user_logs_in_after_creation(self):
        post_data = {
            'username': 'test',
            'email': 'te.st@te.st',
            'first_name': 'Test',
            'last_name': 'Case',
            'password1': 'test123',
            'password2': 'test123',
        }

        response = self.client.post(reverse('rawauth:registration'), post_data)
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('blog:new'))
        self.assertEqual(response.status_code, 200)
