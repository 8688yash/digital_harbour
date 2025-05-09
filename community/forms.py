from django import forms
from .models import UserProfile, Post, Message, Certificate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'skills', 'achievements']

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'file', 'issued_date']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'text', 'image']
