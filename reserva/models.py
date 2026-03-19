from django.db import models

# Create your models here.
#Creamos la clase de Reserva para poder crearla en la base de datos y así se vean visualizadas las reservas que haremos en la aplicación
class Reserva(models.Model):
    nombre = models.CharField(max_length=100) #El máximo de caracteres que puede tener el nombre.
    correo = models.EmailField(max_length=100)#El máximo de caracteres que puede tener el correo.
    huespedes = models.IntegerField()#Pondremos el nº de huespedes estabeclido en el html de reserva.html.
    camas = models.CharField(max_length=50)#Lo mismo que en huespedes.
    fecha_entrada = models.DateField('fecha de entrada: ')#Metodo para poder realizar la fecha de entrada.
    fecha_salida = models.DateField('fecha de salida: ')#Metodo para poder realizar la fecha de salida.

    def __str__(self):
        #Devolvemos el nombre para así saber que reserva es en la base de datos.
        return self.nombre