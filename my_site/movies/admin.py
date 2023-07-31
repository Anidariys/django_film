from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import (
    Category, Ganre, Movie, MovieShot,
    Actor, Rating, RatingStar, Review
)


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Description", widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", )


class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsIniLine(admin.TabularInline):
    model = MovieShot
    extra = 1
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="150" hight="160')

    get_image.short_description = "Image"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft")
    list_display_links = ("title", )
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsIniLine, ReviewInLine]
    save_on_top = True
    save_as = True
    list_editable = ("draft", )
    readonly_fields = ("get_image", )
    form = MovieAdminForm
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"), )
        }),
        (None, {
            "fields": (("description", "get_image"), )
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"), )
        }),
        ("Actors", {
            "classes": ("collapse", ),
            "fields": (("actors", "directors", "ganres", "category"), )
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"), )
        }),
        ("Options", {
            "fields": (("url", "draft"), )
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" hight="118')

    get_image.short_description = "Poster"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "movie", "id")
    list_display_links = ("name", )
    readonly_fields = ("name", "email")


@admin.register(Ganre)
class GanreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Actor)
class ActorwAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" hight="118')

    get_image.short_description = "Image"


@admin.register(Rating)
class RatingwAdmin(admin.ModelAdmin):
    list_display = ("movie", "ip")


@admin.register(MovieShot)
class MovieShotAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" hight="118')

    get_image.short_description = "Image"


admin.site.register(RatingStar)

admin.site.site_title = "Django MOVIES"
admin.site.site_header = "Django MOVIES"
