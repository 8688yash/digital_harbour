from django import forms
from .models import Whitepaper

class WhitepaperForm(forms.ModelForm):
    class Meta:
        model = Whitepaper
        fields = ['title', 'description', 'content_pdf', 'category', 'cover_image']
