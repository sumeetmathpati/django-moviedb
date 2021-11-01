from django.http import JsonResponse
from django.shortcuts import render
from .models import Movie 


def movie_list(request):
    movies = Movie.objects.all()
    data = {'movies': list(movies.values())}
    return JsonResponse(data)
    
def movie_detail(request, pk):
    movie = Movie.objects.get(id=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'rating': movie.rating,
    }
    return JsonResponse(data)
