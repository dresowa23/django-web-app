from django.urls import path
from .import views

#Mostramos las Urls que en este caso iran en la app de Reserva, la cual tambien accedemos por la url.py principal de hotel.
urlpatterns =[
    path('reservar/',views.reserva, name='reservar'),#Ruta de la pagina principal de esta aplicación que es la de reserva y donde podremos hacer dicha reserva.
    path('reserva_confirmada/',views.reserva_confirmada, name='reserva_confirmada')#Ruta para que nos saldra una vez tengamos hecha la reserva.
]