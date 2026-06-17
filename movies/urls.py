from django.urls import path
from movies.views import *


urlpatterns = [
    path('', home.as_view(), name='movie_home'),
    path('add_movie/',add_movie.as_view(), name='add'),
    path('movieapi/', apiview.as_view(), name='api'),
]