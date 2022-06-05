from django.urls import path
from .views import index
from .views import adoptados
from .views import formulario
from .views import galeria
from .views import mision
from .views import vision
from .views import quienessomos
from .views import registrousuario


urlpatterns = [
    path('', index,name="index")
]
urlpatterns = [
    path('', adoptados,name="adoptados")
]
urlpatterns = [
    path('', formulario,name="formulario")
]
urlpatterns = [
    path('', galeria,name="galeria")
]
urlpatterns = [
    path('', mision,name="mision")
]
urlpatterns = [
    path('', vision,name="vision")
]
urlpatterns = [
    path('', quienessomos,name="quinessomos")
]
urlpatterns = [
    path('', registrousuario,name="registrousuario")
]