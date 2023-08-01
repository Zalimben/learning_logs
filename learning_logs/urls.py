"""Define las URLs para learning_logs."""

from . import views
from django.urls import path

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Página para mostrar todos los tópicos
    path('topics/', views.getTopics, name='getTopics'),
    # Página para mostrar los detalles de un tópico
    path('topics/<int:topic_id>/', views.getTopic, name='getTopic'),
    # Página para crear un nuevo tópico
    path('new_topic/', views.newTopic, name='newTopic'),
    # Página para crear una nueva entrada
    path('new_entry/<int:topic_id>/', views.newEntry, name='newEntry'),
    # Página para editar una nueva entrada
    path('edit_entry/<int:entry_id>/', views.editEntry, name='editEntry'),
    path('remove_entry/<int:entry_id>/', views.removeEntry, name='removeEntry'),
]
