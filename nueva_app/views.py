from django.shortcuts import render

def  mostrar_home ( request):
    return render (request, "nueva_app/home.html", {})


def  mostrar_profile( request):
    return render (request, "nueva_app/profile.html", {})

