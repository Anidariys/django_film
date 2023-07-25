from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField(default=0)
    desctiption = models.TextField()
    image = models.ImageField(upload_to="movies/actors")

    def __str__(self):
        return self.name


class Ganre(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, default="")
    description = models.TextField()
    poster = models.ImageField(upload_to="movies/posters")
    year = models.PositiveSmallIntegerField(default=2019)
    country = models.CharField(max_length=50)
    directors = models.ManyToManyField("Actor", related_name="film_director")
    actors = models.ManyToManyField("Actor", related_name="film_actors")
    ganres = models.ManyToManyField("Ganre")
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0)
    fees_in_usa = models.PositiveIntegerField(default=0)
    fees_in_world = models.PositiveIntegerField(default=0)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.review_set.filter(parent__isnull=True)


class MovieShot(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="movie/shots")
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value


class Rating(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey("RatingStar", on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.star} -> {self.movie}"


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=120)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, blank=True, null=True
        )
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} -> {self.movie}"
