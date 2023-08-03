import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from learning_logs.models import Topic


class TopicModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        print("\n=== TopicModelTest ===")
        print("setUpTestData: Definimos los datos de pruebas.")
        user = User.objects.create_user("UsuarioPrueba")
        Topic.objects.create(text='Texto de Prueba', date_added=datetime.UTC, owner=user)

    def setUp(self):
        print("setUp: Se ejecuta al comienzo de cada test.")
        pass

    def test_text_topic(self):
        print("Test 1. Campo texto de topic")
        topic = Topic.objects.get(id=1)
        text = topic.text
        self.assertEqual(text, 'Texto de Prueba')
        self.assertEqual(topic.__str__(), 'Texto de Prueba')

    def test_not_owner_user_filter(self):
        print("Test 2. Filtrar topics por usuario")
        user2 = User.objects.create_user("UsuarioPrueba2")
        topic = Topic.objects.filter(owner=user2)
        self.assertTrue(len(topic) == 0)
