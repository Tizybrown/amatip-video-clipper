from django.contrib import admin
from django.urls import path
from . import views  # Import the views from your project

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', views.home, name='home'),  # Home page
    path('process_clip/', views.process_clip, name='process_clip'),  # Video processing page
]
