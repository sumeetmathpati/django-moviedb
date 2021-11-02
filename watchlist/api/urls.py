from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.MediaListAPI.as_view(), name='media-list'),
    path('platforms/', views.PlatformListAPi.as_view(), name='platforms-list'),
    path('platform/<str:pk>/', views.PlatformDetailsAPI.as_view(), name='platform-detail'),
    path('<str:pk>/', views.MediaDetailAPI.as_view(), name='media-detail'),
]