from django import forms
from WEB.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


    
class registrarUsuario(UserCreationForm):
    username= forms.CharField(label="Ingrese su nombre de usuario")
    email = forms.EmailField(label="Correo electronico")
    password1 = forms.CharField(label="Ingrese la contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Confirme la contraseña",widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
      model = User
      fields = ["username","email","password1","password2","first_name","last_name"]
      

class EditarUsuario(UserCreationForm):
    email = forms.EmailField(label="Corre electronico")
    password1 = forms.CharField(label="ingrere la contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label= "confirme la contraseña",widget=forms.PasswordInput)
    first_name = forms.CharField(label="ingrese su nombre")
    last_name = forms.CharField(label="ingrese su apellido")
    class Meta:
      model = User
      fields = ["email","password1","password2","first_name","last_name"]


class AvatarFormu(forms.ModelForm):
   imagen = forms.ImageField() 
   class Meta:
      model = AvatarImagen
      fields = ["usuario","imagen"]

#form de incidencia
class IncidenciaForm(forms.Form):
    #django coloca un id por defecto
    titulo   = forms.CharField()
    descripcion  = forms.CharField()
    Estado   = forms.CharField()
