from django.urls import path
from .views import (
    CineListView,
    CineDetailView,
    PeliculaListView,
    PeliculaDetailView,
    HorarioListView,
    HorarioDetailView,
    FuncionListView,
    FuncionDetailView,
    UsuarioInteresadoListView,
    UsuarioInteresadoDetailView
)

urlpatterns = [
    path('cines/', CineListView.as_view()),
    path('cines/<int:cine_id>/', CineDetailView.as_view()),
    path('peliculas/', PeliculaListView.as_view()),
    path('peliculas/<int:pelicula_id>/', PeliculaDetailView.as_view()), 
    
    path('horarios/', HorarioListView.as_view()),
    path('horarios/<int:horario_id>/', HorarioDetailView.as_view() ),
    
    
    path('funciones/', FuncionListView.as_view()),
    path('funciones/<int:funcion_id>/', FuncionDetailView.as_view()),
    
    path('usuarios/', UsuarioInteresadoListView.as_view()),
    path('usuarios/<int:usuario_id>/', UsuarioInteresadoDetailView.as_view())

    
]