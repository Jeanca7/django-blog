from django import forms
from .models import Post   #the type of model I want


class PostForm(forms.ModelForm):
    class Meta:
        model=Post #the type of model I want
        exclude = ['published_date', 'author', 'views']