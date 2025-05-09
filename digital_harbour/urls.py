from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from author import views as author_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('community/', include('community.urls')),
    path('author/', include('author.urls')),
    path('publish-book/', author_views.publish_book, name='publish_book'),
    path('create-article/', author_views.create_article, name='create_article'),
    path('whitepapers/', include('whitepapers.urls', namespace='whitepapers')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
