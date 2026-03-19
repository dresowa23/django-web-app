#Proyecto Web- Pacific Hotel

Este proyecta esta realizado en Django. Permite:

- Gestionar las noticias registradas en la base de datos.
- Gestionar y realizar las reservas de manera local en la base de datos.

Mostrare las dependencias necesarias que teneis que instalar para que la aplicación funcione y los pasos a seguir si queremos modificar los modelos de la base de datos, guardarlos o eliminarnos tanto en la base de datos como en el entorno de desarrollo.

##Instalación

A continuación te voy a mostrar los pasos a seguir para que funcione todo perfecto:

1. Descargamos el archivo .ZIP en nuestro ordenador y lo guardamos en el sitio que queramos del ordenador.
2. En la ubicación donde se encuentre el archivo los descomprimimos para poder visualizar todo el contenido.
3. Abrimos el entorno de desarrollo, en este caso utilizo VISUAL CODE, realizamos esta ruta: `Archivo` o `File` ->`Nueva Carpeta` o `Open Folder` -> Seleccionamos nuestro archivo.
4. Una vez ya abierto el archivo, pulsamos CTRL+J y abrimos la terminal y escribimos este comando para abrir el entorno virtual:
   .\env\Scripts\activate .
5. Una vez activado el entorno virtual nos dirigimos a la app principal de hotel escribiendo esto en el terminal 'cd hotel'.
6. Para activar el servidor escribimos 'python manage.py runserver' y seleccionamos la ip que nos aparece en la terminal: 
   http://127.0.0.1:8000/
7. Una vez comprobado que el servidor funciona ya podemos realizar cualquier cosa que queramos con la web.

##Base de datos

Para poder trabajar con la base de datos de manera local, primero necesitamos este comando para poder crear el usuario para gestionar la base. 

Comando para crear usuario: python manage.py createsuperuser
A continuación, te muestro el admin predeterminado que he usado por si quieres tenerlo o quieras crear otro:

###Usuario base de datos

nombre de usuario: Stephen
email: pacifichote@gmail.com
password: Master_d2025

Una vez realizado el usuario, esta es la IP una vez arrancado el servidor para poder trabajar con el admin:
http://127.0.0.1:8000/admin/

##Navegación

Para poder modificar cada url que queramos de nuestra app podemos realizar esta ruta de ejemplo: Reserva -> urls.py y ahi encontraras las Urls y podras hacer lo que quieras.

##Visualización de Paginas

Si quieres modificar la pagina ya sea el HTML o CSS puedes acceder en la carpeta templates para HTML o static para CSS.

##Dependencias

La dependencia principal que tienes que instalar para que puedas modificar el proyecto es esta: pip install django.

##Requisitos
Python: 3.14.0
Django: 6.0