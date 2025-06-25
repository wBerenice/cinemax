from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
import json


db = settings.MONGO_DB

# PELÍCULAS
'''
class PeliculaListView(View):
    def get(self, request):
        peliculas = list(db.peliculas.find({}, {"_id": 0}))
        return JsonResponse(peliculas, safe=False)
   
'''   
@method_decorator(csrf_exempt, name="dispatch")
class PeliculaListView(View):
    def get(self, request):
        peliculas = list(db.peliculas.find({}, {"_id": 0}))
        return JsonResponse(peliculas, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            if "id" not in data or "titulo" not in data:
                return JsonResponse({"error": "Faltan campos obligatorios"}, status=400)

            # Validación de duplicados
            if db.peliculas.find_one({"id": data["id"]}):
                return JsonResponse({"error": "La película ya existe"}, status=409)

            db.peliculas.insert_one(data)
            return JsonResponse({"mensaje": "Película agregada con éxito"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

@method_decorator(csrf_exempt, name="dispatch")
class PeliculaDetailView(View):
    def get(self, request, pelicula_id):
        try:
            pelicula_id = int(pelicula_id)
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)

        pelicula = db.peliculas.find_one({"id": pelicula_id}, {"_id": 0})
        if not pelicula:
            return JsonResponse({"error": "No encontrada"}, status=404)
        return JsonResponse(pelicula)

    def put(self, request, pelicula_id):
        try:
            pelicula_id = int(pelicula_id)
            data = json.loads(request.body)
            result = db.peliculas.update_one({"id": pelicula_id}, {"$set": data})
            if result.matched_count == 0:
                return JsonResponse({"error": "Película no encontrada"}, status=404)
            return JsonResponse({"mensaje": "Película actualizada correctamente"})
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

    def delete(self, request, pelicula_id):
        try:
            pelicula_id = int(pelicula_id)
            result = db.peliculas.delete_one({"id": pelicula_id})
            if result.deleted_count == 0:
                return JsonResponse({"error": "Película no encontrada"}, status=404)
            return JsonResponse({"mensaje": "Película eliminada exitosamente"})
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)
 
 


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
        
