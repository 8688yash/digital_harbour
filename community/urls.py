from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_home, name='community'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='my_profile'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('post/', views.post_view, name='post'),
    path('message/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent'),
    path('search/', views.search_users, name='search_users'),
    path('create/', views.create_post, name='create_post'),
    path('login/', views.login_view, name='login'),
]
