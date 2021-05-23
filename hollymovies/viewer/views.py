from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy



def hello(request, name):
    food = request.GET.get('food', 'Chicken')
    drink = request.GET.get('drink', 'Coke')

    return HttpResponse(f'Hello, world. Nice to meet you {name}. Favorite food and drink: {food} {drink}')


def total_movies(request):

    total_number_movies = Movie.objects.count()

    context = {'total_number_movies': total_number_movies}

    return render(request, template_name='total_movies.html', context=context)


class WelcomeView(TemplateView):
    template_name = 'welcome.html'


class MoviesList(ListView):
    template_name = 'movies_list.html'
    model = Movie
    context_object_name = 'movies'


class CreateMovie(CreateView):
    template_name = 'create_movie.html'
    model = Movie
    success_url = reverse_lazy('movies')
    fields = '__all__'


class DetailMovie(DetailView):
    template_name = 'detail_movie.html'
    model = Movie
    context_object_name = 'movie'


class UpdateMovie(UpdateView):
    template_name = 'update_movie.html'
    model = Movie
    success_url = reverse_lazy('movies')
    fields = '__all__'
    context_object_name = 'movie'


class DeleteMovie(DeleteView):
    template_name = 'delete_movie.html'
    model = Movie
    context_object_name = 'movie'
    success_url = reverse_lazy('movies')






