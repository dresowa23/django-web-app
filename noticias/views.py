from django.shortcuts import render,get_object_or_404
from .models import Noticias

# Create your views here.
#En esta funcion lo que hacemos es unir la clase noticias,creada en models.py, con el html creado para visualizar la noticia.
def noticias(request):
    noticias = Noticias.objects.order_by('-fecha') #He puesto "order_by('-fecha')" para que así se visualice la noticia más reciente.
    context = {'noticias':noticias}
    template = 'noticias.html'
    return render(request,template,context)

#Aquí hacemos lo mismo que en la anterior función pero con el 'noticias_detallada.html',
#además de que así relacionamos cada noticia con su ID
def noticia_detallada(request,noticia_id):
    noticia = get_object_or_404(Noticias, id=noticia_id)#Aqui ponemos el 'get_object_or_404' para evitar cualquier tipo de error si la pagina no existe.
    return render(request,'noticias_detallada.html',{'noticia':noticia})