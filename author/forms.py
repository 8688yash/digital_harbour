from django import forms
from .models import Article, Book
from .models import AuthorProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ArticleForm(forms.ModelForm):
    author_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'e.g. John Doe'
        })
    )

    author_designation = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'e.g. Content Writer, Researcher'
        })
    )

    article_description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-textarea',
            'placeholder': 'Brief overview of the article...',
            'rows': 3
        })
    )

    class Meta:
        model = Article
        fields = ['title', 'topic', 'content_file', 'image', 'image_description']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter article title'
            }),
            'topic': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter article topic'
            }),
            'content_file': forms.ClearableFileInput(attrs={
                'class': 'form-input'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-input'
            }),
            'image_description': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. AI generated, handmade, etc.'
            }),
        }


from django import forms
from .models import Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
    ('fr', 'French'),
    ('es', 'Spanish'),
]

GENRE_CHOICES = [
    ('fiction', 'Fiction'),
    ('non-fiction', 'Non-Fiction'),
    ('poetry', 'Poetry'),
    ('biography', 'Biography'),
    ('science', 'Science'),
    ('technology', 'Technology'),
]

class BookForm(forms.ModelForm):
    genre = forms.ChoiceField(choices=GENRE_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control border border-gray-300 rounded px-4 py-2'
    }))
    language = forms.ChoiceField(choices=LANGUAGE_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control border border-gray-300 rounded px-4 py-2'
    }))
    price = forms.DecimalField(max_digits=6, decimal_places=2, required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control border border-gray-300 rounded px-4 py-2',
        'placeholder': 'e.g. 9.99'
    }))
    tags = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control border border-gray-300 rounded px-4 py-2',
        'placeholder': 'e.g. motivation, sci-fi, AI'
    }))
    author_bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control border border-gray-300 rounded px-4 py-2',
        'placeholder': 'Write a short bio about the author...',
        'rows': 4
    }), required=False)

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control border border-gray-300 rounded px-4 py-2',
        'placeholder': 'Describe your book...',
        'rows': 5
    }))

    class Meta:
        model = Book
        fields = [
            'title', 'description', 'genre', 'language', 'price',
            'tags', 'author_bio', 'manuscript', 'cover_image'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control border border-gray-300 rounded px-4 py-2',
                'placeholder': 'Enter book title'
            }),
            'manuscript': forms.ClearableFileInput(attrs={
                'class': 'form-control border border-gray-300 rounded px-4 py-2'
            }),
            'cover_image': forms.ClearableFileInput(attrs={
                'class': 'form-control border border-gray-300 rounded px-4 py-2'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'enctype': 'multipart/form-data'}
        self.helper.add_input(Submit('submit', 'Publish Book', css_class='bg-green-600 hover:bg-green-700 text-white font-semibold px-6 py-2 rounded'))


class AuthorProfileForm(forms.ModelForm):
    class Meta:
        model = AuthorProfile
        fields = ['profile_image', 'bio', 'expertise', 'certificates']

