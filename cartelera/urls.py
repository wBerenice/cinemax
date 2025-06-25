from django.urls import path
from .views import (
    CineListView,
    PeliculaListView,
    PeliculaDetailView,
    HorarioListView,
    FuncionListView,
    UsuarioInteresadoListView
)

urlpatterns = [
    path('cines/', CineListView.as_view()),
    path('peliculas/', PeliculaListView.as_view()),
    path('peliculas/<int:pelicula_id>/', PeliculaDetailView.as_view()), 
    #path('peliculas/<str:pelicula_id>/', PeliculaDetailView.as_view()), 
    path('horarios/', HorarioListView.as_view()),
    path('funciones/', FuncionListView.as_view()),
    path('usuarios_interesados/', UsuarioInteresadoListView.as_view()),
]