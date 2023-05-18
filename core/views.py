from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages #envia mensajes
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm # formulario personalizado (validacion de errores)
from crispy_forms.helper import FormHelper

# para usar el calendario
import calendar
from django.views import View

from core.models import Event
from django import forms
#from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

from .models import Event

import logging
logger = logging.getLogger('django')


#Importaciones para las vistas de reserva

from core.models import Medico, Especialidad, TipoServicio,Servicio,Event,User,ReservaHora
from core.forms import EventForm


def home(request):   #pagina de inicio
    return render (request, 'home.html')

def acceder(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
        else:
            context['login_form'] = form
    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request,"login.html", context) 

def LogOut(request):
    logout(request)
    return redirect('/')

def registro(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=raw_password)
            #login(request, user) da error
            return redirect('acceder')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'registro.html', context)




#Obtener horas
def agregar_ceros(num):
    return f"{num:02d}"

def generar_opciones_de_tiempo():
    opciones = []
    for hora in range(9,18):
        for minuto in range(00, 60, 60):
            hora_formateada = f"{agregar_ceros(hora)}:{agregar_ceros(minuto)}"
            opciones.append(hora_formateada)
    return opciones

def tomarHoras():
    horasTotales = generar_opciones_de_tiempo()
    reservas = ReservaHora.objects.all()
    horaReservadas =[]
    horaTotal = []
    #crear listas con las horas actuales
    for reservaHoras in reservas:
        horaReservadas.append(reservaHoras.hora)
    for total in horasTotales:
        if total not in horaReservadas:
            horaTotal.append(total)
    return horaTotal

def consultas(request):
    listaMedicos={}
    listaMedicos['medicos']= Medico.objects.all()
    listaMedicos['servicios']= Servicio.objects.all()
    listaMedicos['tipoServicios']= TipoServicio.objects.all()
    listaMedicos['rangos_de_hora']=generar_opciones_de_tiempo()
    listaMedicos['horamedica']= ReservaHora.objects.all()
    listaMedicos['horasLibres']= tomarHoras()
    return render(request,'consultas.html',listaMedicos)


def create_event(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = user
            event.save()
            return redirect('myapp:events_list', user_id=user.id)
    else:
        form = EventForm()
    return render(request, 'myapp/create_event.html', {'form': form, 'user': user})




