from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.MovieListAPI.as_view(), name='movie-list'),
    path('<str:pk>/', views.MovieDetailAPI.as_view(), name='movie-detail'),
]