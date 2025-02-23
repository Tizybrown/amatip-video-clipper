from django.contrib import admin
from django.urls import path, include
from video_clipper import views  # Import the views from the video_clipper app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('video/', include('video_clipper.urls')),  # Video clipping URL
    path('', views.home, name='home'),  # Add this line to handle the root URL
    path('process_clip/', views.process_clip, name='process_clip'),  # clip processing page

]
