"""Define las URLs para learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.getTopics, name='getTopics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.getTopic, name='getTopic'),
]
