from django import forms
from .models import Entry


class BlogForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ["name", "description", "tags"]