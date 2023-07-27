"""Define las urls para users"""
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Incluir las url de autenticación por defecto
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]


