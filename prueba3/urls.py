from django.urls import path
from .views import index, vision, mision, quienessomos, formulario, adoptados, galeria, registrousuario, mod_registrousuario,mostrardatos,del_registrousuario

urlpatterns = [
    path('',index,name="index"),
    path('index.html',index,name="index"),
    path('vision.html',vision,name="vision"),
    path('mision.html',mision,name="mision"),
    path('quienessomos.html',quienessomos,name="quienessomos"),
    path('formulario.html',formulario,name="formulario"),
    path('adoptados.html',adoptados,name="adoptados"),
    path('galeria.html',galeria,name="galeria"),
    path('registrousuario.html',registrousuario,name="registrousuario"),
    path('mod_registrousuario.html/<id>',mod_registrousuario,name="mod_registrousuario"),
    path('del_registrousuario.html/<id>',del_registrousuario,name="del_registrousuario"),
    path('mostrardatos.html',mostrardatos,name="mostardatos"),
]



