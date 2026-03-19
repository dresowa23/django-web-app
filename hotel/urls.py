"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls), #Ruta para poder acceder a la base de datos del sistema y poder trabajar en local desde ella.
    path('reservar/', include('reserva.urls')),#Ruta para la app de reserva. Ponemos "reserva/" para asi evitar conflicto de URLS.
    path('noticias/',include('noticias.urls')),#Ruta para la app de noticias. Sucede lo mismo que con "reserva/", así evitamos conflictos de urls.
    path('', views.inicio,name='inicio'),#Ruta que nos lleva al index, inicio, de la pagina web.
    
]
