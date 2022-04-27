from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Genero de la Movie")

    def __str__(self):
        return self.name

class Movies(models.Model):
    name = models.CharField(max_length=120, help_text="Nombre de la Película")
    genre = models.ManyToManyField(Genre)
    premiere_date = models.DateField(null=False, blank=False)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    execution_time = models.PositiveSmallIntegerField()
    summary = models.TextField(max_length=100, help_text="Descripcion de la Movies")

    def __str__(self):
        return '%s, %s, %s' % (self.name, self.genre, self.director)

    def get_absolute_url(self):
        return reverse('Movie-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'

class Director(models.Model):
    first_name = models.CharField(max_length=100,help_text="Nombre del director", null=False)
    last_name = models.CharField(max_length=100,help_text="Apellido del director",null=False)
    num_movies = models.PositiveSmallIntegerField(default=1,help_text="Numero de Movies Filmadas",null=False)
    date_of_birth = models.DateField(null=True, blank=True,help_text="Edad Nacimiento")
    date_of_death = models.DateField("Died", null=True, blank=True,help_text="Fecha de Fallecimiento")

    WINED_OSCAR = (
        ('s','Si'),
        ('n','No')
    )

    oscars = models.CharField(max_length=1, choices=WINED_OSCAR, default='n', help_text="Indique si ha ganado un oscar",blank=True)

    num_oscars = models.PositiveSmallIntegerField(default=0,help_text="Indique el numero de Oscars Ganados",null=True)

    class Meta:
        ordering = ["first_name"]

    def get_absolute_url(self):
        return reverse('author-details', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

