from django.urls import path
from Capuchino.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    

    #---------------------Receta:
    path('recetas/', receta, name='receta'),
    path('busquedareceta/', buscarReceta, name='buscarReceta'),
    path('busqueda-receta/', busquedaReceta, name='buscar_receta'),
    path('leerReceta/', leerReceta, name='leerReceta'),
    path('eliminarReceta/<id>', eliminarReceta, name='eliminarReceta'),
    path('editarReceta/<id>', editarReceta, name='editarReceta'),


    #----------------------Cheff:
    path('cheffs/', cheff, name='cheff'),
    path('busquedachef/', buscarChef, name='buscarChef'),
    path('busqueda-chef/', busquedaChef, name='buscar_chef'),
    path('leerChefs/', leerChef, name='leerChef'),
    path('eliminarChef/<id>', eliminarChef, name='eliminarChef'),
    path('editarChef/<id>', editarChef, name='editarChef'),


    #----------------------Cliente:
    path('clientes/', cliente, name='cliente'),
    path('busquedacliente/', buscarCliente, name='buscarCliente'),
    path('busqueda-cliente/', busquedaCliente, name='buscar_cliente'),
    path('leerCliente/', leerCliente, name='leerCliente'),
    path('eliminarCliente/<id>', eliminarCliente, name='eliminarCliente'),
    path('editarCliente/<id>', editarCliente, name='editarCliente'),


    #---------------------Restaurants:   
    path('restaurants/', restaurant, name='restaurant'),
    path('busquedarest/', buscarRest, name='buscarRest'),
    path('busqueda-restaurant/', busquedaRest, name='buscar_rest'),
    path('leerRestaurant/', leerRest, name='leerRest'),
    path('eliminarRestaurant/<id>', eliminarRest, name='eliminarRest'),
    path('editarRestaurant/<id>', editarRest, name='editarRest'),

    #----------------------Base de datos y login
    path('editarBase/', editarBase, name='editarBase'),
    path('login/', login_request, name="login" ),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editando_perfil/', editarPerfil, name= 'editarPerfil'),
    
    path('agregar_imagen/', AgregarAvatar, name='agregarAvatar'),
    path('modificar_perfil/', modfPerfil, name='modificarPerfil'),

    path('about/', about, name='about'),

]
