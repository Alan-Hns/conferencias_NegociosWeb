from django.shortcuts import render
from django.http import HttpResponse


def index(request):

   participantes = [
        {
            'nombre': 'Juan',
            'apellido': 'Lopez',
            'correo': 'juan@gmail.com',
            'twitter': 'juan.lopez'
        },
        {
            'nombre': 'Maria',
            'apellido': 'Gomez',
            'correo': 'maria@gmail.com',
            'twitter': 'maria.gomez'
        },
        {
            'nombre': 'Karla',
            'apellido': 'Herrea',
            'correo': 'karla.herrea@gmail.com',
            'twitter': 'karla.herrera'
        },
        {
            'nombre': 'Josue',
            'apellido': 'Alvarez',
            'correo': 'josue@gmail.com',
            'twitter': 'josuetec2003'
        },
    ]

    return render(request, 'registro/index.html', ctx)
