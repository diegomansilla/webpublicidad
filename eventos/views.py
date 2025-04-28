from django.shortcuts import render
from .models import Evento, Sponsor
from datetime import datetime
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def index(request):
    eventos = Evento.objects.prefetch_related('sponsors').order_by('-fecha')  # Últimos eventos primero
    return render(request, 'eventos/index.html', {
        'eventos': eventos,
        'now': datetime.now(),
        })

def eventos_list(request):
    eventos = Evento.objects.all().order_by('-fecha')
    return render(request, 'eventos/eventos_list.html', {'eventos': eventos})

def sponsors_list(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'eventos/sponsors_list.html', {'sponsors': sponsors})

#Temporal
def crear_superusuario(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        return HttpResponse("Superusuario creado!")
    else:
        return HttpResponse("El superusuario ya existe.")