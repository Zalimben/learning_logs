from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Formulario para crear un topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': 'Topico'}


class EntryForm(forms.ModelForm):
    """Formulario para crear una entrada"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Nueva entrada'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
