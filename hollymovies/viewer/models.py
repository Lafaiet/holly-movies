from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    release_date = models.DateTimeField(null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title