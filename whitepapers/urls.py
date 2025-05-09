# whitepapers/urls.py

from django.urls import path
from . import views

app_name = 'whitepapers'

urlpatterns = [
    path('', views.whitepaper_home, name='home'), 
    path('', views.whitepaper_list, name='whitepaper_list'),
    path('submit/', views.submit_whitepaper, name='submit_whitepaper'),
    path('<int:pk>/', views.view_whitepaper, name='view_whitepaper'),
]
