from django.shortcuts import render

def index(request):
    return render(request, 'prueba3/index.html')

def vision(request):
    return render(request, 'prueba3/vision.html')


def mision(request):
    return render(request, 'prueba3/mision.html')

def quienessomos(request):
    return render(request, 'prueba3/quienessomos.html')

def formulario(request):
    return render(request, 'prueba3/formulario.html')

def adoptados(request):
    return render(request, 'prueba3/adoptados.html')

def galeria(request):
    return render(request, 'prueba3/galeria.html')

def registrousuario(request):
    return render(request, 'prueba3/registrousuario.html')
