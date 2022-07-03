from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def prueba( request ):
    context = {}
    return render( request, "mi_mvt/index.html", context)