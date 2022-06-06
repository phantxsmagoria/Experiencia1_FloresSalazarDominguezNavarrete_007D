from django import forms 
from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['pnombre','apellido','email','contraseña','rut','telefono','Direccion','region','comuna']