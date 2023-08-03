from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
class TopicFormTest(TestCase):

    def setUp(self):
        print('\n=== TopicFormTest ===')
        print('Creamos datos iniciales')
        # Creamos 2 usuarios
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

    def test_create_topic(self):
        print('Test 1. Creamos un topic nuevo')
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/new_topic/')

        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)

        response = self.client.post('/new_topic/', data={'text': 'Nuevo Topic test'})
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/topics/')
        self.assertEqual(len(response.context['topics']), 1)
        self.assertEqual(response.context['topics'][0].text, 'Nuevo Topic test')