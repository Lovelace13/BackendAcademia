from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Materia, Aula, Profesor

# Create your views here.
def materias_api(request):
    listMaterias = Materia.objects.all()
    listaAsignaturas = []
    for materia in listMaterias:
        asignaturas = {
            'id': materia.idmateria,
            'titulo': materia.nombre,
            'descripcion': materia.descripcion
        }
        listaAsignaturas.append(asignaturas)

    dataJson = {
        'Asignaturas': listaAsignaturas
    }
    return JsonResponse(dataJson)

def aulas_api(request):
    listaula = Aula.objects.all()
    listaSalon = []
    for aula in listaula:
        salon = {
            'id': aula.idasignatura,
            'codigo': aula.codigo,
            'tema': aula.tema,
            'fecha': aula.fecha,
            'hora': aula.hora,
            'asignatura': aula.idasignatura,
            'profesor': aula.ideducador
        }
        listaSalon.append(salon)

    dataJson = {
        'aulas': listaSalon
    }
    return JsonResponse(dataJson)

def profesor_api(request):
    listprofesor = Profesor.objects.all()
    listaEducador = []
    for profesor in listprofesor:
        educador = {
            'id': profesor.idprofesor,
            'nombre': profesor.nombre,
            'cedula': profesor.cedula,
            'idAsignatura': profesor.idasignatura,
        }
        listaEducador.append(educador)

    dataJson = {
        'Profesores': listaEducador
    }
    return JsonResponse(dataJson)