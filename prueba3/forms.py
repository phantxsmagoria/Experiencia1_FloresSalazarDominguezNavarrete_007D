from django import forms 
from django.forms import ModelForm
from .models import Usuario,Contacto


class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['pnombre','apellido','email','contraseña','rut','telefono','Direccion','region','comuna']

class ContactoForm(ModelForm):

    class Meta:
        model = Contacto
        fields = ['rut','pnombre','apellido','email','telefono','dudas']