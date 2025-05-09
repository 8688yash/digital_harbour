from django.contrib import admin
from .models import AuthorProfile, Article, Book

admin.site.register(AuthorProfile)
admin.site.register(Article)
admin.site.register(Book)

