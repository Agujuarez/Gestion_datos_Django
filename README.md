# Proyecto Django: Gestión de Autores y Libros
![admin Django](/img/admin.png)

Este proyecto es una aplicación web construida con Django para gestionar una base de datos de autores y libros. Los usuarios pueden agregar, ver, editar y eliminar autores, así como los libros asociados a cada autor. La aplicación cuenta con un panel de administración donde se puede gestionar toda la información.

## Caracteristicas
* Gestión de autores: Crear, leer, actualizar y eliminar     autores.
* Gestión de libros: Asignar libros a los autores y gestionarlos desde el panel de administración.
* Interfaz web amigable para interactuar con la base de datos de autores y libros.

## Requisitos

* Python 3.12 o superior
* Django 5.1.2
* Base de datos SQLite (configuración por defecto)
* Virtualenv (opcional, pero recomendado)

## Instalación:

## Crear y activar entorno virtual
Se recomienda usar un entorno virtual para mantener las dependencias aisladas. Si no tienes virtualenv instalado, puedes instalarlo con:
```sh
pip install virtualenv
```
Luego, crea y activa el entorno virtual:
```sh
virtualenv venv
source venv/bin/activate
```

## Instalar las dependencias
Con el entorno virtual activado, instala las dependencias del proyecto utilizando el archivo [requirements.txt](requirements.txt):
```sh
pip install -r requirements.txt
```

## Realizar las migraciones de la base de datos
Aplica las migraciones para crear las tablas necesarias en la base de datos:
```sh
python manage.py migrate
```

## Crear un superusuario
Para poder acceder al panel de administración, necesitas crear un superusuario:
```sh
python manage.py createsuperuser
```
Sigue las instrucciones para establecer el nombre de usuario, correo electrónico y contraseña.

## Ejecutar el servidor de desarrollo
Inicia el servidor local de Django:
```sh
python manage.py runserver
```
La aplicación estará disponible en http://127.0.0.1:8000/.

## Uso
### Panel de administración
Accede al panel de administración en http://127.0.0.1:8000/admin/ y utiliza las credenciales del superusuario que creaste para ingresar.

A continuación, verás el siguiente panel donde podrás gestionar los autores y libros:


### Listado de Autores
En el panel de administración puedes agregar, editar y eliminar autores. Cada autor puede tener varios libros asociados.

### Detalles del Autor
Para cada autor, puedes ver los libros asociados. A continuación se muestra un ejemplo de cómo se gestionan los autores y sus libros:

* Claudio Zuchovicki (Economista, Argentino)
* John Ronald Reuel Tolkien (Escritor, Inglés)
* George R.R. Martin (Escritor, Estadounidense)
### Estructura de la Base de Datos
#### Autor
* Nombre: Nombre completo del autor.
* Fecha de nacimiento: La fecha en que nació el autor.
* Fecha de fallecimiento: Si corresponde, la fecha en que falleció el autor.
* Profesión: Ocupación principal del autor (ej. Escritor, Economista).
* Nacionalidad: País de origen del autor.
#### Libro
* Título: Nombre del libro.
* Cita: Fragmento o cita destacada del libro.
* Autor: Relación con el autor que escribió el libro.

### Archivos Relevantes
* [blog/urls.py:](blog/urls.py) Archivo que contiene las rutas de la aplicación.
* [blog/views.py:](blog/views.py) Vistas que manejan las solicitudes HTTP para la página de autores y libros.
* [templates/index.html](templates/index.html): Página principal que muestra la lista de autores.
* [templates/autor.html:](templates/autor.html) Página que muestra los detalles de un autor y sus libros.
