from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from mi_mvt.models import Familiares

def prueba( request ):
    context = {}
    if request.GET:
        context["nombre"] = request.GET["nombre"]
    return render( request, "mi_mvt/index.html", context)

def info_familiar ( request):
    context = {}
    context["familiares"] = Familiares.objects.all()
    return render( request, "mi_mvt/lista_familiar.html", context)


