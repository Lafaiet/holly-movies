from django.db import models
from .constants import COUNTRIES, LANGUAGES
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50, choices=LANGUAGES)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateTimeField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True, choices=COUNTRIES)
    languages = models.ManyToManyField(Language)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)
    directors = models.ManyToManyField(Person, related_name='directors')
    stars = models.ManyToManyField(Person, related_name='stars')

    def __str__(self):
        return self.title


class Profile(models.Model):
    biography = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    watch_list = models.ManyToManyField(Movie)

    def __str__(self):
        return self.user.username
