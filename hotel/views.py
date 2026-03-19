from django.shortcuts import render

#con esta funcion lo que hacemos es que la pagina principal se carge el index, que seria la pagina base
def inicio(request):
    return render(request,'index.html') 