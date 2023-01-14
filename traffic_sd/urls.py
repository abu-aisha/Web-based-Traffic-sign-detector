from django.urls import path, include
from traffic_sd import views

app_name = 'traffic_sd'
urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    ]
