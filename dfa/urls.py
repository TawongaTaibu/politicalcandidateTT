from django.contrib import admin
from django.urls import path, include
from . import views

#This is the name of our application
app_name = 'dfa'

#Each path matches and communicates with the template that it shares it's name with
urlpatterns = [
    path('', views.home, name = 'home'),
    path('registration/', views.registration, name = 'registration'),
    path('login/', views.login, name = 'login'),
    path('news_list/', views.news_list, name = 'news_list'),
    path('News/<int:id>/', views.News_View, name = 'News_View'),
 ]
 

