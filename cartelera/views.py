from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
import json


db = settings.MONGO_DB

# PELÍCULAS
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
@method_decorator(csrf_exempt, name="dispatch")
class CineListView(View):
    def get(self, request):
        cines = list(db.cines.find({}, {"_id": 0}))
        return JsonResponse(cines, safe=False)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            if "id" not in data or "nombre" not in data:
                return JsonResponse({"error": "Faltan campos obligatorios"}, status=400)
            if db.cines.find_one({ "id": data["id"] }):
                return JsonResponse({"error": "Cine ya registrado"}, status=409)
            db.cines.insert_one(data)
            return JsonResponse({"mensaje": "Cine agregado exitosamente"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        
        
@method_decorator(csrf_exempt, name="dispatch")
class CineDetailView(View):
    def get(self, request, cine_id):
        try:
            cine_id = int(cine_id)
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)

        cine = db.cines.find_one({ "id": cine_id }, { "_id": 0 })
        if not cine:
            return JsonResponse({ "error": "Cine no encontrado" }, status=404)
        return JsonResponse(cine)

    def put(self, request, cine_id):
        try:
            cine_id = int(cine_id)
            data = json.loads(request.body)
            result = db.cines.update_one({ "id": cine_id }, { "$set": data })
            if result.matched_count == 0:
                return JsonResponse({ "error": "Cine no encontrado" }, status=404)
            return JsonResponse({ "mensaje": "Cine actualizado correctamente" })
        except (ValueError, json.JSONDecodeError):
            return JsonResponse({ "error": "Datos inválidos" }, status=400)

    def delete(self, request, cine_id):
        try:
            cine_id = int(cine_id)
            result = db.cines.delete_one({ "id": cine_id })
            if result.deleted_count == 0:
                return JsonResponse({ "error": "Cine no encontrado" }, status=404)
            return JsonResponse({ "mensaje": "Cine eliminado exitosamente" })
        except ValueError:
            return JsonResponse({ "error": "ID inválido" }, status=400)


# HORARIOS

@method_decorator(csrf_exempt, name="dispatch")
class HorarioListView(View):
    def get(self, request):
        horarios = list(db.horarios.find({}, {"_id": 0}))
        return JsonResponse(horarios, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            if "id" not in data or "dia" not in data or "hora" not in data:
                return JsonResponse({"error": "Faltan campos obligatorios"}, status=400)
            if db.horarios.find_one({ "id": data["id"] }):
                return JsonResponse({"error": "Horario ya existente"}, status=409)
            db.horarios.insert_one(data)
            return JsonResponse({"mensaje": "Horario agregado exitosamente"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        
        
@method_decorator(csrf_exempt, name="dispatch")
class HorarioDetailView(View):
    def get(self, request, horario_id):
        try:
            horario_id = int(horario_id)
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)

        horario = db.horarios.find_one({ "id": horario_id }, { "_id": 0 })
        if not horario:
            return JsonResponse({"error": "Horario no encontrado"}, status=404)
        return JsonResponse(horario)

    def put(self, request, horario_id):
        try:
            horario_id = int(horario_id)
            data = json.loads(request.body)
            result = db.horarios.update_one({ "id": horario_id }, { "$set": data })
            if result.matched_count == 0:
                return JsonResponse({"error": "Horario no encontrado"}, status=404)
            return JsonResponse({"mensaje": "Horario actualizado correctamente"})
        except (ValueError, json.JSONDecodeError):
            return JsonResponse({"error": "Datos inválidos"}, status=400)

    def delete(self, request, horario_id):
        try:
            horario_id = int(horario_id)
            result = db.horarios.delete_one({ "id": horario_id })
            if result.deleted_count == 0:
                return JsonResponse({"error": "Horario no encontrado"}, status=404)
            return JsonResponse({"mensaje": "Horario eliminado exitosamente"})
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)        

# FUNCIONES

@method_decorator(csrf_exempt, name="dispatch")
class FuncionListView(View):
    def get(self, request):
        funciones = list(db.funciones.find({}, {"_id": 0}))
        return JsonResponse(funciones, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            if "id" not in data or "pelicula" not in data or "cine" not in data:
                return JsonResponse({"error": "Faltan campos obligatorios"}, status=400)
            if db.funciones.find_one({ "id": data["id"] }):
                return JsonResponse({"error": "Función ya registrada"}, status=409)
            db.funciones.insert_one(data)
            return JsonResponse({"mensaje": "Función agregada exitosamente"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        
@method_decorator(csrf_exempt, name="dispatch")
class FuncionDetailView(View):
    def get(self, request, funcion_id):
        try:
            funcion_id = int(funcion_id)
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)

        funcion = db.funciones.find_one({ "id": funcion_id }, { "_id": 0 })
        if not funcion:
            return JsonResponse({"error": "Función no encontrada"}, status=404)
        return JsonResponse(funcion)

    def put(self, request, funcion_id):
        try:
            funcion_id = int(funcion_id)
            data = json.loads(request.body)
            result = db.funciones.update_one({ "id": funcion_id }, { "$set": data })
            if result.matched_count == 0:
                return JsonResponse({"error": "Función no encontrada"}, status=404)
            return JsonResponse({"mensaje": "Función actualizada correctamente"})
        except (ValueError, json.JSONDecodeError):
            return JsonResponse({"error": "Datos inválidos"}, status=400)

    def delete(self, request, funcion_id):
        try:
            funcion_id = int(funcion_id)
            result = db.funciones.delete_one({ "id": funcion_id })
            if result.deleted_count == 0:
                return JsonResponse({"error": "Función no encontrada"}, status=404)
            return JsonResponse({"mensaje": "Función eliminada exitosamente"})
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)

# USUARIOS INTERESADOS
@method_decorator(csrf_exempt, name="dispatch")
class UsuarioInteresadoListView(View):
    def get(self, request):
        usuarios = list(db.usuariosInteresados.find({}, {"_id": 0}))
        return JsonResponse(usuarios, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)
            if "id" not in data or "nombre" not in data or "correo" not in data:
                return JsonResponse({"error": "Faltan campos obligatorios"}, status=400)
            if db.usuariosInteresados.find_one({ "id": data["id"] }):
                return JsonResponse({"error": "Usuario ya registrado"}, status=409)
            db.usuariosInteresados.insert_one(data)
            return JsonResponse({"mensaje": "Usuario registrado exitosamente"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        
@method_decorator(csrf_exempt, name="dispatch")
class UsuarioInteresadoDetailView(View):
    def get(self, request, usuario_id):
        try:
            usuario_id = int(usuario_id)
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)

        usuario = db.usuariosInteresados.find_one({ "id": usuario_id }, {"_id": 0})
        if not usuario:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)
        return JsonResponse(usuario)

    def put(self, request, usuario_id):
        try:
            usuario_id = int(usuario_id)
            data = json.loads(request.body)
            result = db.usuariosInteresados.update_one({ "id": usuario_id }, { "$set": data })
            if result.matched_count == 0:
                return JsonResponse({"error": "Usuario no encontrado"}, status=404)
            return JsonResponse({"mensaje": "Usuario actualizado correctamente"})
        except (ValueError, json.JSONDecodeError):
            return JsonResponse({"error": "Datos inválidos"}, status=400)

    def delete(self, request, usuario_id):
        try:
            usuario_id = int(usuario_id)
            result = db.usuariosInteresados.delete_one({ "id": usuario_id })
            if result.deleted_count == 0:
                return JsonResponse({"error": "Usuario no encontrado"}, status=404)
            return JsonResponse({"mensaje": "Usuario eliminado exitosamente"})
        except ValueError:
            return JsonResponse({"error": "ID inválido"}, status=400)
        
