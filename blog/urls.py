from django.urls import path
from django.views.generic import TemplateView
from . import views
from author import views as author_views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy_policy'),
    path('terms/', TemplateView.as_view(template_name="blog/terms.html"), name="terms"),
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('library/', views.library_view, name='library'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
    path('dashboard/', views.author_dashboard, name='author_dashboard'),
    path('freebies/', views.freebies, name='freebies'),
    path('mission/', views.mission, name='mission'),
    path('vision/', views.vision, name='vision'),
    path('who-we-are/', views.who_we_are, name='who_we_are'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('community/', views.community, name='community_home'),
    path('author/', views.author_dashboard, name='author_dashboard'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('search/', views.search_blogs, name='search_blogs'),
    path('blogs/<int:blog_id>/view/', views.view_pdf_by_id, name='view_pdf'),
    path('blogs/<slug:slug>/view/', views.view_pdf, name='view_pdf'),
    path('blogs/<int:blog_id>/view/', views.view_pdf, name='blog_view_pdf'),
    path('publish-book/', author_views.publish_book, name='publish_book'),
    path('create-article/', author_views.create_article, name='create_article'),
    path('', views.whitepaper_home, name='whitepaper_home'),
    path('category/<str:category>/', views.whitepaper_home, name='whitepaper_category'),  # if whitepaper_home is the right view
    path('view/<int:pk>/', views.whitepaper_list, name='whitepaper_detail'),
    path('submit/', views.submit_whitepaper, name='submit_whitepaper'),


]
