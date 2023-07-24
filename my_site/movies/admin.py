from django.contrib import admin

from .models import (
    Category, Ganre, Movie, MovieShot,
    Actor, Rating, RatingStar, Review
)


admin.site.register(Category)
admin.site.register(Ganre)
admin.site.register(Movie)
admin.site.register(MovieShot)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Review)
