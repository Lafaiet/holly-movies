from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Profile
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import SignUpForm
from django.db.models import Q


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

    def get_queryset(self):

        search = self.request.GET.get('search', None)

        if search:
            queryset = Movie.objects.filter(Q(title__contains=search) | Q(genre__name__contains=search))
        else:
            queryset = Movie.objects.all()

        return queryset



class CreateMovie(PermissionRequiredMixin, CreateView):
    template_name = 'create_movie.html'
    model = Movie
    success_url = reverse_lazy('movies')
    fields = '__all__'
    permission_required = 'viewer.add_movie'


class DetailMovie(DetailView):
    template_name = 'detail_movie.html'
    model = Movie
    context_object_name = 'movie'


class UpdateMovie(PermissionRequiredMixin, UpdateView):
    template_name = 'update_movie.html'
    model = Movie
    success_url = reverse_lazy('movies')
    fields = '__all__'
    context_object_name = 'movie'
    permission_required = 'viewer.change_movie'


class DeleteMovie(PermissionRequiredMixin, DeleteView):
    template_name = 'delete_movie.html'
    model = Movie
    context_object_name = 'movie'
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'


class SignUpView(CreateView):
    template_name = 'create_profile.html'
    success_url = reverse_lazy('movies')
    form_class = SignUpForm

class DetailProfile(DetailView):
    template_name = 'detail_profile.html'
    model = Profile
    context_object_name = 'profile'






