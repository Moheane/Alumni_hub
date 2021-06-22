from django.urls import path
from .import views

urlpatterns = [
    path('', views.landingPage, name='Homepage'),
    path('home/', views.HomePage, name='HomePage'),
    path('about/', views.AboutPage, name='AboutPage'),
     path('contacts/', views.contactsPage, name='contactsPage'),
     
]