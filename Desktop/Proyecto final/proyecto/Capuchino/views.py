from django.shortcuts import render
from .models import *
from Capuchino.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin #para vistas basadas en clases
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones

def inicio(request):

    return render(request, 'Capuchino/inicio.html', {'imagen': obtenerAvatar(request)})

def about(request):

    return render(request, 'Capuchino/about.html', {'imagen': obtenerAvatar(request)})

@login_required
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!= 0:
        imagen=lista[0].imagen.url

    else:
        imagen='/Avatares/Avatares/fondo.jpg'
    return imagen



@login_required
def editarBase(request):
    return render(request, 'Capuchino/editarBase.html', {'imagen': obtenerAvatar(request)})



#------------------------Bloque Recetas
@login_required
def receta(request):
    if request.method == "POST":
        form= RecetaForm(request.POST,)
        if form.is_valid():
            informacion= form.cleaned_data

            nombre= informacion['nombre']
            dificultad=informacion['dificultad']
            pasos=informacion['pasos']
       

            receta= Receta(nombre=nombre, dificultad=dificultad, pasos=pasos)
            receta.save()
            return render(request,'Capuchino/inicio.html', {'mensaje':'Receta guardada correctamente', 'imagen': obtenerAvatar(request)})
        else:
            return render(request, 'Capuchino/recetas.html', {"form":form, 'imagen': obtenerAvatar(request)})
    else:
        form= RecetaForm()
    
    return render(request, 'Capuchino/recetas.html', {"form":form, 'imagen': obtenerAvatar(request)})


def buscarReceta(request):
    return render(request, 'Capuchino/buscarReceta.html', {'imagen': obtenerAvatar(request)})

def busquedaReceta(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]
        receta= Receta.objects.filter(nombre__icontains=nombre)
        return render(request, 'Capuchino/resultadoReceta.html', {'recetas':receta, 'imagen': obtenerAvatar(request)})

    else:
        return render(request, 'Capuchino/buscarReceta.html', {'mensaje_2':'por favor ingrese una receta', 'imagen': obtenerAvatar(request)})


@login_required
def leerReceta(request):
    receta= Receta.objects.all()
    return render(request, 'Capuchino/leerReceta.html', {'recetas':receta, 'imagen': obtenerAvatar(request)})

@login_required
def eliminarReceta(request, id):
    receta= Receta.objects.get(id=id)
    receta.delete()

    receta= Receta.objects.all()
    return render(request, 'Capuchino/leerReceta.html', {'mensaje':'Receta eliminado correctamente', 'recetas':receta, 'imagen': obtenerAvatar(request)})

@login_required
def editarReceta(request, id):
    receta= Receta.objects.get(id=id)
    if request.method=='POST':
        form= RecetaForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            receta.nombre= informacion['nombre']
            receta.dificultad= informacion['dificultad']
            receta.pasos= informacion['pasos']
            receta.save()
            receta= Receta.objects.all()
            return render(request, 'Capuchino/leerReceta.html', {'mensaje':'Receta editada correctamente', 'recetas':receta, 'imagen': obtenerAvatar(request)})
            
    else:
        formulario= RecetaForm(initial={'nombre':receta.nombre , 'dificultad':receta.dificultad, 'pasos':receta.pasos})
    return render(request, 'Capuchino/editarReceta.html', {'form':formulario, 'recetas':receta, 'imagen': obtenerAvatar(request)})

#------------------------Bloque Cheff

@login_required
def cheff(request):
    if request.method == "POST":
        form= CheffForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            email= informacion['email']
            restaurant= informacion['restaurant']
            especialidad= informacion['especialidad']

            cheff= Cheff(nombre=nombre, apellido=apellido, email=email, restaurant=restaurant, especialidad=especialidad)
            cheff.save()
            return render(request,'Capuchino/inicio.html', {'mensaje':'Chef creado correctamente', 'imagen': obtenerAvatar(request)})
        else:
            return render(request, 'Capuchino/cheffs.html', {"form":formulario, 'imagen': obtenerAvatar(request)})
    else:
        formulario= CheffForm()
    
    return render(request, 'Capuchino/cheffs.html', {"form":formulario, 'imagen': obtenerAvatar(request)},)

def buscarChef(request):
    return render(request, 'Capuchino/buscarChef.html', {'imagen': obtenerAvatar(request)})


def busquedaChef(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]
        chefs= Cheff.objects.filter(nombre__icontains=nombre)
        return render(request, 'Capuchino/resultadoChef.html', {'chefs':chefs, 'imagen': obtenerAvatar(request)})

    else:
        return render(request, 'Capuchino/buscarChef.html', {'mensaje_2':'por favor ingrese un Chef', 'imagen': obtenerAvatar(request)})

@login_required
def leerChef(request):
    chef= Cheff.objects.all()
    return render(request, 'Capuchino/leerChef.html', {'chefs':chef, 'imagen': obtenerAvatar(request)})

@login_required
def eliminarChef(request, id):
    chef= Cheff.objects.get(id=id)
    chef.delete()

    chef= Cheff.objects.all()
    return render(request, 'Capuchino/leerChef.html', {'mensaje':'Chef eliminado correctamente', 'chefs':chef, 'imagen': obtenerAvatar(request)})

@login_required
def editarChef(request, id):
    chef= Cheff.objects.get(id=id)
    if request.method=='POST':
        form= CheffForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            chef.nombre= informacion['nombre']
            chef.apellido= informacion['apellido']
            chef.email= informacion['email']
            chef.restaurant= informacion['restaurant']
            chef.especialidad= informacion['especialidad']

            chef.save()
            chef= Cheff.objects.all()
            return render(request, 'Capuchino/leerChef.html', {'mensaje':'Chef editado correctamente', 'chefs':chef, 'imagen': obtenerAvatar(request)})
            
    else:
        formulario= CheffForm(initial={'nombre':chef.nombre , 'apellido':chef.apellido, 'email':chef.email, 'restaurant':chef.restaurant, 'especialidad':chef.especialidad})
    return render(request, 'Capuchino/editarChef.html', {'form':formulario, 'chefs':chef, 'imagen': obtenerAvatar(request)})

#------------------------Bloque Restaurats

@login_required
def restaurant(request):
    if request.method == "POST":
        form= RestaurantForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data

            nombre= informacion['nombre']
            direccion= informacion['direccion']
            estrellas= informacion['estrellas']

            restaurant= Restaurant(nombre=nombre, direccion=direccion, estrellas=estrellas)
            restaurant.save()
            return render(request,'Capuchino/inicio.html', {'mensaje':'Restaurant añadido correctamente', 'imagen': obtenerAvatar(request)})
        else:
            return render(request, 'Capuchino/restaurants.html', {"form":formulario, 'imagen': obtenerAvatar(request)})
    else:
        formulario= RestaurantForm()
    
    return render(request, 'Capuchino/restaurants.html', {"form":formulario, 'imagen': obtenerAvatar(request)},)

def buscarRest(request):
    return render(request, 'Capuchino/buscarRest.html', {'imagen': obtenerAvatar(request)})


def busquedaRest(request):

    if request.GET["pepito"]:

        nombre= request.GET["pepito"]
        rest= Restaurant.objects.filter(nombre__icontains=nombre)
        return render(request, 'Capuchino/resultadoRest.html', {'rests':rest, 'imagen': obtenerAvatar(request)})

    else:
        return render(request, 'Capuchino/buscarRest.html', {'mensaje_2':'por favor ingrese un restaurant', 'imagen': obtenerAvatar(request)})

@login_required
def leerRest(request):
    rest= Restaurant.objects.all()
    return render(request, 'Capuchino/leerRest.html', {'rests':rest, 'imagen': obtenerAvatar(request)})

@login_required
def eliminarRest(request, id):
    rest= Restaurant.objects.get(id=id)
    rest.delete()

    rest= Restaurant.objects.all()
    return render(request, 'Capuchino/leerRest.html', {'mensaje':'Restaurant eliminado correctamente', 'rests':rest, 'imagen': obtenerAvatar(request)})

@login_required
def editarRest(request, id):
    rest= Restaurant.objects.get(id=id)
    if request.method=='POST':
        form= RestaurantForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            rest.nombre= informacion['nombre']
            rest.direccion= informacion['direccion']
            rest.estrellas= informacion['estrellas']           
            rest.save()
            rest= Restaurant.objects.all()
            return render(request, 'Capuchino/leerRest.html', {'mensaje':'Restaurant editado correctamente', 'rests':rest, 'imagen': obtenerAvatar(request)})
            
    else:
        formulario= RestaurantForm(initial={'nombre':rest.nombre , 'direccion':rest.direccion, 'estrellas':rest.estrellas})
    return render(request, 'Capuchino/editarRest.html', {'form':formulario, 'rests':rest, 'imagen': obtenerAvatar(request)})

#------------------------Bloque Clientes
@login_required
def cliente(request):
    if request.method == "POST":
        form= ClienteForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data

            nombre= informacion['nombre']
            apellido= informacion['apellido']
            email= informacion['email']
            reseña= informacion['reseña']

            cliente= Cliente(nombre=nombre, apellido=apellido, email=email, reseña=reseña)
            cliente.save()
            return render(request,'Capuchino/inicio.html', {'mensaje':'Éxito al enviar la reseña', 'imagen': obtenerAvatar(request)})
        else:
            return render(request, 'Capuchino/clientes.html', {"form":formulario, 'imagen': obtenerAvatar(request)},)
    else:
        formulario= ClienteForm()
    
    return render(request, 'Capuchino/clientes.html', {"form":formulario, 'imagen': obtenerAvatar(request)},)

def buscarCliente(request):
    return render(request, 'Capuchino/buscarCliente.html', {'imagen': obtenerAvatar(request)})

def busquedaCliente(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]
        cliente= Cliente.objects.filter(nombre__icontains=nombre)
        return render(request, 'Capuchino/resultadoCliente.html', {'clientes':cliente, 'imagen': obtenerAvatar(request)})

    else:
        return render(request, 'Capuchino/buscarCliente.html', {'mensaje_2':'por favor ingrese un usuario', 'imagen': obtenerAvatar(request)})

@login_required
def leerCliente(request):
    cliente= Cliente.objects.all()
    return render(request, 'Capuchino/leerCliente.html', {'clientes':cliente, 'imagen': obtenerAvatar(request)})

@login_required
def eliminarCliente(request, id):
    cliente= Cliente.objects.get(id=id)
    cliente.delete()

    cliente= Cliente.objects.all()
    return render(request, 'Capuchino/leerCliente.html', {'mensaje':'Cliente eliminado correctamente', 'clientes':cliente, 'imagen': obtenerAvatar(request)})

@login_required
def editarCliente(request, id):
    cliente= Cliente.objects.get(id=id)
    if request.method=='POST':
        form= ClienteForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            cliente.nombre= informacion['nombre']
            cliente.apellido= informacion['apellido']
            cliente.email= informacion['email']
            cliente.reseña= informacion['reseña']     
            cliente.save()
            cliente= Cliente.objects.all()
            return render(request, 'Capuchino/leerCliente.html', {'mensaje':'Cliente editado correctamente', 'clientes':cliente, 'imagen': obtenerAvatar(request)})
            
    else:
        formulario= ClienteForm(initial={'nombre':cliente.nombre , 'apellido':cliente.apellido, 'email':cliente.email, 'reseña':cliente.reseña})
    return render(request, 'Capuchino/editarCliente.html', {'form':formulario, 'clientes':cliente, 'imagen': obtenerAvatar(request)})

#----------------------Bloque Login

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu= form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            usuario=authenticate(username=usu, password=clave) #trae usuario y contraseña de la BD

            if usuario is not None:
                login(request, usuario)
                return render(request, 'Capuchino/inicio.html', {'mensaje':f'Bienvenido {usuario}', 'imagen': obtenerAvatar(request)})
            
            else:
                return render(request, 'Capuchino/login.html', {'mensaje_2':'Usuario o contraseña incorrectos', "form":form})
        else:
            return render(request, 'Capuchino/login.html', {'mensaje_2':'Usuario o contraseña incorrectos', 'form':form})
    else:
        form=AuthenticationForm()
    
    return render(request, 'Capuchino/login.html', {'form':form})

def register(request):
    if request.method =='POST':
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, 'Capuchino/inicio.html', {'mensaje': f'Usuario {username} creado exitosamente'})
        else:
            return render(request, 'Capuchino/register.html', {'form':form, 'mensaje': 'Error al crear usuario'})
             
    else:
        form= RegistroUsuarioForm()
    return render(request, 'Capuchino/register.html', {'form':form}) 


@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=='POST':
        form=UserEditForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            usuario.email=info['email']
            usuario.password1=info['password1']
            usuario.password2=info['password2']
            usuario.first_name=info['first_name']
            usuario.last_name=info['last_name']
            usuario.save()
            return render(request, 'Capuchino/inicio.html', {'mensaje':'Perfil editado correctamente', 'imagen': obtenerAvatar(request)})         
        else:
            return render(request, 'Capuchino/editar_usuario.html', {'form':form, 'nombreusuario': usuario.username , 'mensaje_2':'Error al editar perfil', 'imagen': obtenerAvatar(request) })

    else:
        form=UserEditForm(instance=usuario)
        return render(request, 'Capuchino/editar_usuario.html', {'form': form, 'nombreusuario': usuario.username, 'imagen': obtenerAvatar(request)})



@login_required
def modfPerfil (request):
    return render( request, 'Capuchino/modificarperfil.html', {'usuario': request.user, 'imagen': obtenerAvatar(request)})



@login_required
def AgregarAvatar(request):
    if request.method == 'POST':
        form= AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo= Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar= Avatar(user=request.user, imagen=request.FILES['imagen'])
            avatar.save()
            return render(request, 'Capuchino/inicio.html', {'mensaje':'Avatar añadido correctamente','imagen': obtenerAvatar(request)})
        else:
            return render( request, 'Capuchino/agregaravatar.html', {'form':form, 'usuario': request.user, 'imagen': obtenerAvatar(request)})
    else:
        form= AvatarForm()
        return render( request, 'Capuchino/agregaravatar.html', {'form':form, 'usuario': request.user, 'imagen': obtenerAvatar(request)})
