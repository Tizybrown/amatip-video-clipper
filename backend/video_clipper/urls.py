from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('process_clip/', views.process_clip, name='process_clip'),
]
