from django.urls import re_path as url
# from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'^$', views.index, name='index'),
    url(r'^movies/$', views.MovieListView.as_view(), name='movie'),
    url(r'^movies/(?P<pk>\d+)$', views.MovieDetailView.as_view(), name='movie-detail'),
}

