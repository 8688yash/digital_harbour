from django.contrib import admin
from .models import Blog, AuthorProfile, LibraryItem, Subscribe
from .models import Freebie, MarketplaceItem, CommunityPost


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created_at')
    list_filter = ('published',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(LibraryItem)
class LibraryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'uploaded_at')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category', 'uploaded_at')

@admin.register(Subscribe)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', )


@admin.register(Freebie)
class FreebieAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')

@admin.register(MarketplaceItem)
class MarketplaceItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'available')

@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'group')

from django.contrib import admin
from .models import GalleryImage

admin.site.register(GalleryImage)
