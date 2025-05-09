from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ("maritime", "Maritime"),
    ("business", "Business"),
    ("technology", "Technology"),
    ("ai", "Artificial Intelligence"),
    ("web_dev", "Web Development"),
    ("app_dev", "App Development"),
    ("smm", "Social Media Marketing"),
    ("email_marketing", "Email Marketing"),
    ("seo", "Search Engine Optimization"),
    ("ads", "Google Ads & Analytics"),
    ("cybersecurity", "Cybersecurity"),
    ("blockchain", "Blockchain"),
    ("data_science", "Data Science"),
]

class Whitepaper(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    content_pdf = models.FileField(upload_to='whitepapers/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    cover_image = models.ImageField(upload_to='whitepapers/covers/', null=True, blank=True)
    reviewed = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False) 

    def __str__(self):
        return self.title

class WhitepaperCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name