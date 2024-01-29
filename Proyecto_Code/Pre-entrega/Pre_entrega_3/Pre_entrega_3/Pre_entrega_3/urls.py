"""
URL configuration for Pre_entrega_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WEB.views import *
from django.contrib.auth.views import LogoutView # cerrar sesion
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #inicio de la web
    path('',inicio, name="inicio"),
    #Login de la web
    path('login/',InicioSesion,name="login"),
    #Logout de la web
    path('logout/',CerrarSesion,name="logout"),
    #Registrar de la web
    path('regis/',Registro,name="registro"),
    #EditarPerfil de la web
    path('edit/',EditarPerfil,name="editar"),
    #EditarPerfil de la web
    path('avatar/',AgregarAvatar,name="avatar"),
    #ventana incidencias de la web
    path('inci/',ticket,name="inci"),
    #ventana incidencias de la web
    path('neinci/',CrearIncidencia,name="new_inci"),
    #ventana incidencias de la web
    path('businci/',BuscarIncidencia,name="bus_inci"),
    path('actinci/<id_old>/',actualizar_inci,name="act_inci"),
    path('elinci/<id_old>/',eliminar_inci,name="elim_inci"),
    path('elinci/<id_old>/',eliminar_inci,name="elim_inci"),
    path('info/',quienes_somos,name="info"),
     path('contacto/',contacto,name="contacto"),
   

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)