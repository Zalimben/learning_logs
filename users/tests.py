from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class LoginView(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('\n=== LoginView ===')

    def test_view_url_exists(self):
        print('Test 1. Login Page')
        response = self.client.get('/users/login/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_HTTP404_for_invalid_url(self):
        print('Test 2. Página 404')
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        login = self.client.login(username='test_user1', password='1X<ISRUkw+tuK')
        response = self.client.get('temas')
        self.assertEqual(response.status_code, 404)


    def test_HTTP404_for_no_logged_user(self):
        print('Test 3. Página 404')
        response = self.client.get('temas')
        self.assertEqual(response.status_code, 404)
