from django.db import models

# Create your models here.

class Usuario(models.Model):
    pnombre =models.CharField(max_length=25, verbose_name='Primer Nombre')
    apellido = models.CharField(max_length=25,verbose_name='Apellido')
    email = models.CharField(max_length=25,verbose_name='Email')
    contraseña = models.CharField(max_length=25,verbose_name='Contraseña')
    rut = models.CharField(primary_key=True, max_length=25,verbose_name='RUT')
    telefono = models.CharField(max_length=25,verbose_name='Teléfono')
    Direccion = models.CharField(max_length=25,verbose_name='Dirección')
    region = models.CharField(max_length=25,verbose_name='Región')
    comuna = models.CharField(max_length=25,verbose_name='Comuna')

    def __str__(self):
        return self.rut