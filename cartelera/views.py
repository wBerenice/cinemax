from django.http import JsonResponse
from django.views import View
from django.conf import settings

db = settings.MONGO_DB

# PELÍCULAS
class PeliculaListView(View):
    def get(self, request):
        peliculas = list(db.peliculas.find({}, {"_id": 0}))
        return JsonResponse(peliculas, safe=False)

class PeliculaDetailView(View):
    def get(self, request, pelicula_id):
        pelicula = db.peliculas.find_one({"id": int(pelicula_id)}, {"_id": 0})
        if pelicula:
            return JsonResponse(pelicula)
        return JsonResponse({"error": "No encontrada"}, status=404)

# CINES
class CineListView(View):
    def get(self, request):
        cines = list(db.cines.find({}, {"_id": 0}))
        return JsonResponse(cines, safe=False)

# HORARIOS
class HorarioListView(View):
    def get(self, request):
        horarios = list(db.horarios.find({}, {"_id": 0}))
        return JsonResponse(horarios, safe=False)

# FUNCIONES
class FuncionListView(View):
    def get(self, request):
        funciones = list(db.funciones.find({}, {"_id": 0}))
        return JsonResponse(funciones, safe=False)

# USUARIOS INTERESADOS
class UsuarioInteresadoListView(View):
    def get(self, request):
        usuarios = list(db.usuariosInteresados.find({}, {"_id": 0}))
        return JsonResponse(usuarios, safe=False)