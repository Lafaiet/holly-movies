from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def hello(request, name):
    food = request.GET.get('food', 'Chicken')
    drink = request.GET.get('drink', 'Coke')

    return HttpResponse(f'Hello, world. Nice to meet you {name}. Favorite food and drink: {food} {drink}')


def total_movies(request):

    total_number_movies = Movie.objects.count()

    return HttpResponse(f'Total number of movies in database is {total_number_movies}')
