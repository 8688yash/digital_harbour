from django.contrib import admin
from .models import Whitepaper, WhitepaperCategory  # make sure you also import your models

@admin.register(Whitepaper)
class WhitepaperAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'is_approved', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('is_approved', 'category', 'created_at')
    ordering = ('-created_at',)

@admin.register(WhitepaperCategory)
class WhitepaperCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
