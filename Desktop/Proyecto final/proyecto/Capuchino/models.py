from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Cliente(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    reseña= models.CharField(max_length=2500)

    def __str__(self):
        return self.nombre+" "+self.apellido

class Receta(models.Model):
    now= datetime.now()
    formatedDay = now.strftime("%Y/%m/%d")

    nombre= models.CharField(max_length=40)
    dificultad= models.CharField(max_length=50)
    pasos= models.CharField(max_length=2500)
    dia = models.CharField(max_length=50, default=formatedDay)

    def __str__(self):
        return "Nombre:  " +self.nombre+" ----   Creada la fecha:  "+ self.dia



class Cheff(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()
    restaurant= models.CharField(max_length=30)
    especialidad= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.apellido


class Restaurant(models.Model):
    nombre= models.CharField(max_length=50)
    direccion= models.CharField(max_length=30)
    estrellas= models.IntegerField()

    def __str__(self):
        return self.nombre+' de '+str(self.estrellas)+' estrellas'

class Avatar(models.Model):
    imagen= models.ImageField(upload_to='Avatares')
    user= models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
