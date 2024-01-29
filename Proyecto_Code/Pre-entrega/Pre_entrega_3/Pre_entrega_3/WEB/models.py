from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Incidencia(models.Model):
    #django coloca un id por defecto
    titulo   = models.CharField(max_length=40)
    descripcion  = models.CharField(max_length=100)
    Estado   = models.CharField(max_length=20)
    fecha_creacion   = models.DateField
    fecha_modificacion  = models.DateField
   
class Comentarios(models.Model):
    comentario = models.CharField(max_length=300)
    fecha = models.DateField
    

class GruposUsuarios(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #me refiero a un usuario creado
    sector  = models.CharField(max_length=20)

class AvatarImagen(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #me refiero a un usuario creado
    imagen= models.ImageField(upload_to="avatares",null=True, blank=True)