from django.db import models

# Create your models here.
#Creamos la clase noticias para que en nuestra base de datos podamos agregar,eliminar o modificar cualquier noticia que queramos importar.
class Noticias(models.Model):
    titulo = models.CharField(max_length=100)#El máximo de caracteres para el titulo.
    texto_noticia = models.CharField(max_length=100000)#Lo mismo pero para el texto de la noticia.
    fecha = models.DateTimeField('fecha de publicacion: ')#Nos permite visualizar la fecha de publicación de la noticia

    def __str__(self) -> str:
        #Devolvemos el titulo de la noticia para asi visualizarlo en el panel de administracion de la base de datos.
        return self.titulo
        