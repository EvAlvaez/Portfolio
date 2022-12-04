from django.shortcuts import render
from django.conf import settings
from mainapp.models import Proyectos

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })

def habilidades(request):
    return render(request, 'mainapp/habilidades.html', {
        'title': 'Habilidades'
    })

def proyectos(request):
    proyectos=Proyectos.objects.all()
    return render(request, 'mainapp/proyectos.html', {
        'title': 'Proyectos',
        'proyectos': proyectos
    })

def recorrido(request):
    return render(request, 'mainapp/recorrido.html', {
        'title': 'Recorrido'
    })

