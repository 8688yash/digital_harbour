from django import forms
from .models import Blog, LibraryItem
from django.contrib.auth.models import User

class blogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'slug', 'pdf_file', 'tags']

class LibraryItemForm(forms.ModelForm):
    class Meta:
        model = LibraryItem
        fields = ['title', 'description','pdf_file', 'category']

class SubscriberForm(forms.Form):
    email = forms.EmailField()

class AuthorRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']