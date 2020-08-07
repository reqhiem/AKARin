from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
# Import models
from .models import Documento

@login_required
def home(request):
    documentos = Documento.objects.all()
    return render(request, "myapp/home.html", {"documentos": documentos ,"titulo": "Bienvenido"})

#Para la busqueda
@login_required
def busqueda(request):
    return render(request, 'myapp/busqueda.html', {"titulo": "Busqueda"})

#View que procesará el pedido de busqueda
@login_required
def buscar(request):
    busca = request.GET.get("search")
    fecha_desde= request.GET.get("fecha_desde")
    fecha_hasta= request.GET.get("fecha_hasta")
    date=""
    if not fecha_hasta:
        if not fecha_desde:
            if not busca:
                return render(request, 'myapp/busqueda.html', {'date' : date})
            elif busca:
                date = Documento.objects.filter(
                    Q(nombre__icontains = busca) |
                    Q(tipo__icontains = busca) |
                    Q(tag__icontains = busca)
                ).distinct()
                return render(request, 'myapp/busqueda.html', {'date':date})
            
        elif fecha_desde:
            if not busca:
                date= Documento.objects.filter(loaded__gte=fecha_desde)
                return render(request, 'myapp/busqueda.html', {'date':date})
            elif busca:
                date= Documento.objects.filter( 
                    Q(nombre__icontains = busca) |
                    Q(tipo__icontains = busca) |
                    Q(tag__icontains = busca), loaded__gte=fecha_desde,
                ).distinct()
                return render(request, 'myapp/busqueda.html', {'date':date})
    elif fecha_hasta:
        if fecha_desde:
            if busca:
                date= Documento.objects.filter( Q(nombre__icontains = busca) | Q(tipo__icontains = busca) | Q(tag__icontains = busca),loaded__range=[fecha_desde, fecha_hasta]).distinct()
                return render(request, 'myapp/busqueda.html', {'date':date})
            elif not busca:
                date = Documento.objects.filter(loaded__range=[fecha_desde, fecha_hasta])
                return render(request, 'myapp/busqueda.html', {'date':date})

@login_required
def cargar(request):
    if request.method == "POST":

        name = request.POST["nombre"]
        typ = request.POST["tipo"]
        etiqueta = request.POST["tag"]
        fil = request.FILES["filedoc"]

        Documento.objects.create(nombre=name, tipo=typ, tag=etiqueta, doc=fil)
        return render(request, 'myapp/cargar.html', {"titulo": "Subir"})

    return render(request, 'myapp/cargar.html', {"titulo": "Subir"})

#view para cargar al servidor
def loading(request):
    pass

@login_required
def help(request):
    return render(request, 'myapp/help.html', {"titulo": "Ayuda"})
@login_required
def perfile(request):
    return render(request, 'myapp/profile.html', {"titulo": "Perfil de usuario"})