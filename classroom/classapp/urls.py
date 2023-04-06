from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
    path('register', views.register, name='register.html'),
    path('login', views.login, name='login.html'),
    path('logout', views.logout, name='logout'),
    path('home', views.view_class, name='/home.html'),
    path('create_class', views.create_class, name='/create_class'),
    path('join_class', views.join_class, name='join_class')
]