from django.contrib.auth.models import User
from django.test import TestCase

from .forms import TopicForm, EntryForm
from .models import Topic


class TopicFormValidationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("\n=== TopicFormValidationTest ===")

    def test_form_is_empty(self):
        print('Test 1. El form está vacío')
        form = TopicForm()
        self.assertTrue(form.fields['text'].label == 'Topico')

    def test_form_text_max_length(self):
        print('Test 2. Longitud máxima mayor')
        text = ('There are many variations of passages of Lorem Ipsum available, but the majority have suffered '
                'alteration in some form, by injected humour, or randomised words which dont look even slightly believable. '
                'If you are going to use a passage of Lorem Ipsum, you need to be sure there is not anything embarrassing '
                'hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined '
                'chunks as necessary, making this the first true generator on the Internet. '
                'It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, '
                'to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free '
                'from repetition, injected humour, or non-characteristic words etc.')
        form = TopicForm(data={'text': text})
        self.assertFalse(form.is_valid())

    def test_form_text_max_length_valid(self):
        print('Test 3. Happy Path')
        text = 'Computer Science'
        form = TopicForm(data={'text': text})
        self.assertTrue(form.is_valid())

    def test_form_is_valid_empty(self):
        print('Test 4. Está vació')
        text = ''
        form = TopicForm(data={'text': text})
        self.assertFalse(form.is_valid())


class EntryFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("\n=== EntryFormTest ===")

    def test_form_is_not_empty(self):
        print('Test 1. El form muestra un mensaje de ayuda')
        form = EntryForm()
        self.assertTrue(form.fields['text'].label == 'Nueva entrada')


class TopicView(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('\n=== TopicView ===')

    def test_view_url_need_auth(self):
        print('Test 1. Topic Page')
        response = self.client.get('/topics/')
        self.assertEquals(response.status_code, 302)


class TopicListViewAuth(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('\n=== TopicListViewAuth ===')

    def setUp(self):
        print('Creamos datos iniciales')
        # Creamos 2 usuarios
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

        # Creamos los topics
        test_topic1 = Topic.objects.create(text='Computer Science', owner=test_user1)
        test_topic2 = Topic.objects.create(text='Biología', owner=test_user2)
        test_topic3 = Topic.objects.create(text='Química', owner=test_user2)
        test_topic1.save()
        test_topic2.save()
        test_topic3.save()

    def test_redirect_if_not_logged_in(self):
        print('Test 1. Redirección correcta si no está autenticado')
        response = self.client.get('/topics/')
        self.assertRedirects(response, '/users/login/?next=/topics/')

    def test_logged_in_uses_correct_template(self):
        print('Test 2. Redirección correcta si está autenticado')
        login = self.client.login(username='testuser2', password='2HJ1vRV0Z&3iD')
        response = self.client.get('/topics/')

        self.assertEqual(str(response.context['user']), 'testuser2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'learning_logs/topics.html')

        self.assertEqual(len(response.context['topics']), 2)
        self.assertEqual(response.context['topics'][0].text, 'Biología')
        self.assertEqual(response.context['topics'][1].text, 'Química')

