from django.urls import path
from Job import views


urlpatterns = [
     path('jobs/', views.jobView, name='JobPage'),
]