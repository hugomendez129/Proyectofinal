from django.shortcuts import render
from django.http import HttpResponse
from WEB.forms import *
from WEB.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def inicio(request):
    #mantener la info de quien esta autenticado
    usuario_autenticado = request.user
    #y la envio al html para tener actualizada la pag del usuario
    return render(request, "inicio.html",{'mensaje': usuario_autenticado})

#funcion de login
def InicioSesion(request):
    if request.method ==  "POST": #si el usuario hace click en el boton
          formulario = AuthenticationForm(request, data = request.POST) #obtener la info del user pass
          if formulario.is_valid():
              info = formulario.cleaned_data
              usuario= info["username"]
              contra= info["password"]
              #metodo de las diapositicas
              #usuario = formulario.cleaned_data.get('username')
              #contra = formulario.cleaned_data.get('password')
              #usamos auten
              user= authenticate(username=usuario, password=contra)
              if user is not None:
                  login(request, user)
                  return render(request,"inicio.html", {"mensaje":f"{usuario}"})
              else:
                  return render(request,"inicion.html", {"mensaje":f"Error, datos incorrectos"}) 
          else:
              return render(request,"inicio.html", {"mensaje":f"Error, datos incorrectos"})
    else:
        formulario = AuthenticationForm() 
    return render(request,"login.html", {"formu":formulario})
#funcion de logout
def CerrarSesion(request):
    logout(request)
    return render(request,"inicio.html")
#funcion registro
def Registro(request):#solo usuario pass
    if request.method ==  "POST": #si el usuario hace click en el boton
        formulario=registrarUsuario(request.POST)
        if formulario.is_valid():
            info= formulario.cleaned_data
            username= info["first_name"]
            formulario.save()
            return render(request,"inicio.html", {"mensaje":f"Bienvenido {username}"})
    
        formulario=registrarUsuario(request.POST)     
    else:
        formulario=registrarUsuario() 
    return render(request,"registro.html",{"formu":formulario})

#editar perfil
def EditarPerfil(request):
    usuario_actual=request.user #busco el usuario conectado
    
    if request.method ==  "POST": #si el usuario hace click en el boton
        usuario_autenticado = request.user
        formulario=EditarUsuario(request.POST)
        if formulario.is_valid():
            info= formulario.cleaned_data
            usuario_actual.first_name= info["first_name"]
            usuario_actual.last_name= info["last_name"]
            usuario_actual.email= info["email"]
            usuario_actual.set_password(info["password1"]) #actualizamos pass
            usuario_actual.save()
            return render(request,"inicio.html")
    
        formulario=EditarUsuario(request.POST)     
    else:
        usuario_autenticado = request.user
        
       #formulario=EditarUsuario()#si no quiero traer datos actuales
        formulario=EditarUsuario(initial={"first_name":usuario_actual.first_name,
                                             "last_name":usuario_actual.last_name,
                                             "email":usuario_actual.email}) 
        contexto={'mensaje': usuario_autenticado,'formu':formulario}    

    return render(request,"editar_usuario.html",contexto)

#vista para Avatar
def AgregarAvatar(request):
    if request.method ==  "POST":
        formulario=AvatarFormu(request.POST,request.FILES)
        if formulario.is_valid():
            info= formulario.cleaned_data
            avatar = AvatarImagen(usuario=request.user,imagen=info['imagen'])
            avatar.save()
            return render(request,"inicio.html")
    else:
        formulario=AvatarFormu()
    return render(request,"avatar.html",{'formu':formulario})



#IR A LA PANTALLA DE INCIDENCIAS
def ticket(request):
    usuario_autenticado = request.user
    return render(request, "incidencias.html",{'mensaje': usuario_autenticado})

#CREAR NUEVA INCIDENCIA
def CrearIncidencia(request):
    if request.method == "POST":
        nuevo_form = IncidenciaForm(request.POST) #mostramos un formulario vacio
        if nuevo_form.is_valid():
            info = nuevo_form.cleaned_data
            nueva_inci=Incidencia(titulo   = info["titulo"] ,
                                  descripcion = info["descripcion"] ,
                                  Estado   =info["Estado"].upper()
                                  )
            nueva_inci.save()
            return render(request,"incidencias.html" )
    else:
        nuevo_form=IncidenciaForm()  
    return render(request,"nueva_inci.html",{"mi_formu":nuevo_form})

#BUSCAR INCIDENCIA
def BuscarIncidencia(request):
    if request.method == "GET":
        Incidencia_pedida = request.GET.get("Estado", "")
        Incidencia_pedida = Incidencia_pedida.upper()
        if Incidencia_pedida:
            resultados_inci = Incidencia.objects.filter(Estado__icontains=Incidencia_pedida)
            return render(request, "Ver_resultados.html", {"incidencia": resultados_inci, "Incidencia_pedida": Incidencia_pedida})
    return render(request, "Busqueda_inci.html", {"Incidencia_pedida": ""})

def actualizar_inci(request,id_old):
    id_escogido = Incidencia.objects.get(id=id_old)
    #le damos click al boto
    if request.method == "POST":
        nuevo_form = IncidenciaForm(request.POST) #mostramos un formulario vacio
        if nuevo_form.is_valid():
            info = nuevo_form.cleaned_data
            #actualizo
            id_escogido.titulo= info["titulo"]
            id_escogido.descripcion=info["descripcion"]
            id_escogido.Estado=info["Estado"].upper()
            id_escogido.save()
            return render(request,"inicio.html" )
        
    else:
        nuevo_form=IncidenciaForm(initial={"titulo":id_escogido.titulo,"descripcion":id_escogido.descripcion,
                                           "Estado":id_escogido.Estado})  
    return render(request,"editar_incidencia.html",{"mi_formu":nuevo_form,"id":id_old})

def quienes_somos(request):
     return render(request, "quienes_somos.html")

def contacto(request):
     return render(request, "contacto.html")


def eliminar_inci(request,id_old):
    inci = Incidencia.objects.get(id=id_old)
    inci.delete()
    return render(request, "eliminar_inci.html")



