from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    """Un tema que el usuario está aprendiendo."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Un elemento aprendido de un tema"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # extra information
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Una representación del modelo."""
        return f"{self.text[:50]}..."
