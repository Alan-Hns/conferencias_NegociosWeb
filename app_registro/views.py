from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

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

def index(request):

    #clase del 24/05/2021

    #import pdb; pdb.set_trace()

    #Parametros GET almacenados en variables de python
    # nombre = request.GET.get('nombre')
    # apellido = request.GET.get('apellido')
    # edad = request.GET.get('edad')
    # return HttpResponse(f'Buenas noches {nombre} {apellido}, su edad es: {edad} años???')

    #clase del 25/05/2021
    #name = request.GET.get('name')

    # variable GET          : name
    # variable de python    : n
    #variable de plantilla  : x


    # Enviar valores a la plantilla a traves del contexto

    # Recibir por GET los parametros para calcular la couta de un prestamo bancario
    # monto: m, tasa: r, plazo: n

    # paso 1
    # m = int(request.GET.get('m'))
    # r = int(request.GET.get('r'))
    # n = int(request.GET.get('n'))

    # # paso 2: preparar los datos para suministrarlos a la formula
    # r = r / 100 / 12
    # n = n * 12

    # # paso 3: aplicar la formula: c = (m * r) / (1 - (1 + r) ** -n)

    # c = (m * r) / (1 - (1 + r) ** -n)

    # ctx = {
    #     'couta': c
    # }

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        twitter = request.POST.get('twitter')

        participantes.append({
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'twitter': twitter
        })

        ctx = {
            'participantes': participantes
        }

        # return HttpResponse('El participante ha sido registrado')
        return render(request, 'registro/index.html', ctx)
    else:
        # contexto que va para la plantilla
        ctx = {
            'participantes': participantes
        }

        return render(request, 'registro/index.html', ctx)

