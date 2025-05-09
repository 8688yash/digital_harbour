from django.db import models
from django.contrib.auth.models import User

class AuthorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author_profile')
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='authors/', default='default_author.png')
    expertise = models.CharField(max_length=255)
    achievements = models.TextField(blank=True, null=True)
    certificates = models.FileField(upload_to='certificates/', blank=True, null=True)  # ✅ Add this line


class Article(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('published', 'Published'),
    ]
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    content_file = models.FileField(upload_to='articles/')
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    image_description = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    manuscript = models.FileField(upload_to='books/')
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=10)
    tags = models.CharField(max_length=100, blank=True)
    author_bio = models.TextField(blank=True)
    download_link = models.URLField(blank=True, null=True)


