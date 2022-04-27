from django.contrib import admin
from .models import Genre, Movies, Director

"""Minimal registration of Models.
admin.site.register(Movies)
admin.site.register(Director)
"""
admin.site.register(Genre)

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'display_genre','premiere_date', 'execution_time')
    list_filter = ('director', 'premiere_date')

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'num_movies', 'num_oscars')
#    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    fieldsets = (
        ('Personals', {
            'fields': ('first_name', 'last_name', 'num_movies', 'date_of_birth', 'date_of_death')
        }),
        ('Premiere', {
            'fields': ('oscars', 'num_oscars')
        }),
    )

admin.site.register(Director, DirectorAdmin)

