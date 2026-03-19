from django.shortcuts import render,redirect
from .models import Reserva
# Create your views here.

#Con esta función lo que hacemos es el metodo para registrar y enviar los datos a la base de datos.
def reserva(request):
    
    #Si el boton, en este caso reservar, es un POST se realiza este metodo.
    if request.method == 'POST':
        #Lo que hacemos aquí es que con los parametros del formulario de la clase reserva, los mandamos con POST y con GET los obtenemos y visualizamos en la base de datos.
        Reserva.objects.create(
            nombre = request.POST.get('nombre'),
            correo = request.POST.get('correo'),
            huespedes = request.POST.get('huespedes'),
            camas = request.POST.get('camas'),
            fecha_entrada = request.POST.get('fecha_entrada'),
            fecha_salida = request.POST.get('fecha_salida'),
        )
        #Una vez que se haga la reserva nos mandara al html de 'reserva_confirmada.html' para asi confirmar que hicimos la reserva.
        return redirect('reserva_confirmada')
    #Nos permite mostrar la pagina de 'reserva.html' si no se hace la reserva correctamente.
    return render(request,'reserva.html')

#Función que nos deja ver la pagina 'reserva_confirmada.html'
def reserva_confirmada(request):
    return render(request,'reserva_confirmada.html')

#Misma función que la anterior
def inicio(request):
    return render(request,'index.html')