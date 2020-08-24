from django import forms
from django.forms import ModelForm

from s_blogs.models import Topic, Entry


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea({'cols': 80})}