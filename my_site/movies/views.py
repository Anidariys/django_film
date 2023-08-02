from django.db.models import Q
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Actor, Movie, Ganre
from .forms import ReviewForm


class GanreYear:
    def get_ganres(self):
        return Ganre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MovieView(GanreYear, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MoviDeatailView(GanreYear, DetailView):
    model = Movie
    slug_field = "url"


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(GanreYear, DetailView):
    model = Actor
    template_name = "movies/actor.html"
    slug_field = "name"


class FilterMoviesView(GanreYear, ListView):
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(ganres__in=self.request.GET.getlist("ganre"))
        )
        return queryset