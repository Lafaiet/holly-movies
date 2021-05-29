"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import hello, total_movies, WelcomeView, MoviesList, \
    CreateMovie, DetailMovie, UpdateMovie, DeleteMovie

from django.conf.urls.static import static
from django.conf import settings
from django.urls import include


urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('admin/', admin.site.urls),
    path('hello/<name>', hello),
    path('total', total_movies, name='total'),
    path('welcome', WelcomeView.as_view(), name='welcome'),
    path('movies', MoviesList.as_view(),  name='movies'),
    path('movies/create', CreateMovie.as_view(),  name='create_movie'),
    path('movies/<int:pk>', DetailMovie.as_view(),  name='detail_movie'),
    path('movies/<int:pk>/update', UpdateMovie.as_view(),  name='update_movie'),
    path('movies/<int:pk>/delete', DeleteMovie.as_view(),  name='delete_movie'),
    path('accounts/', include('django.contrib.auth.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
