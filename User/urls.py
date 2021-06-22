from django.urls import path
from User import views 
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    
    path('register/', views.registerView, name='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='User/logout.html'), name='user-logout'),
    path('profile/', views.profileView, name='user-profile'),
]