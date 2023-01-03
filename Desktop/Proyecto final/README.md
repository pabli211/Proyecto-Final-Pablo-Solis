
# CAPUCHINO, UN BLOG DELICIOSO



En mi proyecto decidí crear un blog dedicado a la gastronomía, un 'ida y vuelta' entre restaurants, comenzales y cheffs. A demas el blog cuenta con una basse de datos dedicada a que los usuarios u chefs puedan compartir recetas. 
El proyecto cuenta con una aplicaciòn llamada 'Capuchino'. En ella podremos encontrar una serie de .html los cuales tomando su estructura de .css logran estructutar una web que sirve como interfaz para que el usuario pueda ingrresar a una base de datos que contiene el proyecto y asi ser almacenados y consultados.

#### La aplicaión cuenta con la seguiente estructura:
    
    
## App Capuchino ---- url: <http://localhost:8000/Capuchino/> :
    
### Templates con los que realicè Herencia:
- 'padre.html'
- 'padre1.html'
- 'padre2.html'

### Templates utilizados para la carga de datos al sistema y como pagina principal de cada sección:
- 'recetas.html', posee vista ----- url: 'recetas/'
- 'cheffs.html', posee vista ----- url: 'cheffs/'
- 'clientes.html', pose vista ----- url: 'clientes/'
- 'restaurants.html', posee vista ----- url 'restaurats/'

### Templates utilizados para la consulta de datos:

1. Class 'Cheff':
- 'buscarChef.html', posee vista ----- url:'busquedachef/'
- 'resultadoChef.html', posee vista ----- url:'busqueda-chef/'
- 'leerChef.html', posee vista ----- url:'leerChefs/'
            
2. Class 'Cliente':
- 'buscarCliente.html', posee vista ----- url:'busquedacliente/'
- 'resultadoCliente.html', posee vista ----- url:'busqueda-cliente/'
- 'leerCliente.html', posee vista ----- url:'leerCliente/'

3. Class 'Restaurant':
- 'buscarRest.html', posee vista ----- url:'busquedarest/'
- 'resultadoRest.html', posee vista ----- url:'busqueda-restaurant/'
- 'leerRest.html', posee vista ----- url:'leerRestaurant/'

4. Class 'Receta':
- 'buscarReceta.html', posee vista ----- url: 'busquedareceta/''busqueda-receta/'
- 'resultadoReceta.html', posee vista ----- url:'busqueda-receta/'
- 'leerReceta.html', posee vista ----- url:'leerReceta/'



### Templates utilizados para la alterar la base de datos:

1. Class 'Cheff':
- 'editarChef.html', posee vista ----- url:'eliminarChef/<id>'  ---- elimina elemento de la base de datos por id
- 'resultadoChef.html', posee vista ----- url:'editarChef/<id>' ---- edita datos guarados en la base de datos por id
                        
2. Class 'Cliente':
- 'editarCliente.html', posee vista ----- url:'eliminarCliente/<id>'---- elimina elemento de la base de datos por id
- 'resultadoCliente.html', posee vista ----- url:'editarCliente/<id>'---- edita datos guarados en la base de datos por id

3. Class 'Restaurant':
- 'editarRest.html', posee vista ----- url:'eliminarRestaurant/<id>'---- elimina elemento de la base de datos por id
- 'resultadoRest.html', posee vista ----- url:'editarRestaurant/<id>'---- edita datos guarados en la base de datos por id

4. Class 'Receta':
- 'editarReceta.html', posee vista ----- url:'editarReceta/<id>'---- elimina elemento de la base de datos por id
- 'resultadoReceta.html', posee vista ----- url:'eliminarReceta/<id>'---- edita datos guarados en la base de datos por id

A todos estos templates podemos acceder desde el hipervinculo que encontramos en <http://localhost:8000/Capuchino/inicio> el cual nos enviará al template 'editarBase.html' donde en el encontraremos una serie de botones para acceder a botones que nos redigirán en base a la 'class' que seleccionemos a cada vista de la base de datos para su posterior modificación


## Acceso a URL 'admin' del proyecto

Se puede ingresar bajo las credenciales **{'usuario': coder ; 'contraseña':house}** a la url <http://localhost:8000/admin> a la visualización que la vista
que nos brinda Django como un 'superuser'. En ella podremos modificar datos de la base, eliminarlos, añadirlo y otras funciones aun no exploradas.



# Funcionamiento
El video de funcionamiento de la pagina se puede ver en: 

<https://www.youtube.com/watch?v=DXeqzSc6eu4&ab_channel=PabloSolis>

# ACLARACIÒN

recomiendo recorrer la pàgina desde lo que yo considero que es la vista principal (inicio) del proyecto la cual podremos acceder desde <http://localhost:8000/Capuchino/inicio>

### PD: 
cabe aclarar que localhost:8000 puede ser variable en otras PC's
 