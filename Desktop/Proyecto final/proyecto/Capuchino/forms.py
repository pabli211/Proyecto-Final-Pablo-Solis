from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    reseña= forms.CharField(max_length=2500)

class RecetaForm(forms.Form):
    nombre= forms.CharField(max_length=40)
    dificultad= forms.CharField(max_length=50)
    pasos= forms.CharField(max_length=2500)


class CheffForm(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()
    restaurant= forms.CharField(max_length=30)
    especialidad= forms.CharField(max_length=50)

class RestaurantForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    direccion= forms.CharField(max_length=30)
    estrellas= forms.IntegerField()


class RegistroUsuarioForm(UserCreationForm):
    first_name= forms.CharField(label="Nombre")
    last_name= forms.CharField(label="Apellido")
    email= forms.EmailField()
    password1= forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['username','first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields} #para cada uno de estos campos, le asigna un valor vacio



class UserEditForm(UserCreationForm):
    first_name= forms.CharField(label="Modificar Nombre")
    last_name= forms.CharField(label="Modificar Apellido")
    email= forms.EmailField()
    password1= forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields} #para cada uno de estos campos, le asigna un valor vacio


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label='imagen')