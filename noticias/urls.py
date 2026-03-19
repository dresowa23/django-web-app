from django.urls import path
from .import views

#Mostramos las rutas que corresponden con la app de Noticias, la cual tambien accedemos por la url.py principal de hotel.
urlpatterns = [
    path('', views.noticias, name='noticias'),#Ruta principal de noticias, donde se veran las noticias.
    path('<int:noticia_id>/',views.noticia_detallada,name='noticia_detallada')#Ruta donde se vera la noticia y el ID de dicha noticia en la base de datos.
]