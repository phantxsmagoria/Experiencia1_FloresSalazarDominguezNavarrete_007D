from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm

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
    datos = {'form': UsuarioForm()}
    if request.method== 'POST': 
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    
    return render(request, 'prueba3/registrousuario.html',datos)
    

def consultadatos(request):
    return render(request, 'prueba3/consultadatos.html')

def mostrardatos(request):
    usuario = Usuario.objects.all()
    datos = {'usuario': usuario}
    return render(request, 'prueba3/mostrardatos.html', datos)