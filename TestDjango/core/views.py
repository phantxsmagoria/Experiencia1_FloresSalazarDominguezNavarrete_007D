from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'core/index')

def formulario(request):

    return render(request, 'core/formulario')

def galeria(request):

    return render(request, 'core/galeria')

def adoptados(request):

    return render(request, 'core/adoptados')

def mision(request):

    return render(request, 'core/mision')

def vision(request):

    return render(request, 'core/vision')

def quienessomos(request):

    return render(request, 'core/quienessomos')

def registrousuario(request):

    return render(request, 'core/registrousuario')

