from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.author_welcome, name='author_welcome'),
    path('setup/', views.author_profile_setup, name='profile_setup'),
    path('dashboard/', views.author_dashboard, name='author_dashboard'),
    path('create-article/', views.create_article, name='create_article'),
    path('publish-book/', views.publish_book, name='publish_book'),
    path('create/', views.create_author_profile, name='create_author_profile'),
]
