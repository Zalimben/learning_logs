from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Formulario para crear un topic"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Formulario para crear una entrada"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
