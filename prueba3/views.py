from django.shortcuts import render,redirect
from .models import Usuario, Contacto
from .forms import UsuarioForm, ContactoForm

def index(request):
    return render(request, 'prueba3/index.html')

def vision(request):
    return render(request, 'prueba3/vision.html')


def mision(request):
    return render(request, 'prueba3/mision.html')

def quienessomos(request):
    return render(request, 'prueba3/quienessomos.html')

def formulario(request):
    datos = {'form':ContactoForm()}
    if request.method== 'POST': 
        formulario = ContactoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    return render(request, 'prueba3/formulario.html',datos)

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
    

def mod_registrousuario(request,id):
    usuario = Usuario.objects.get(rut=id)
    datos = {'form':UsuarioForm(instance=usuario)}
    if request.method== 'POST':
        formulario= UsuarioForm(data=request.POST,instance=usuario)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificación Exitosa"
    return render(request, 'prueba3/mod_registrousuario.html',datos)

def mostrardatos(request):
    usuario = Usuario.objects.all()
    datos = {'usuario': usuario}
    return render(request, 'prueba3/mostrardatos.html', datos)

def del_registrousuario(request,id):
    usuario = Usuario.objects.get(rut=id)
    usuario.delete()
    return redirect(to="index")
