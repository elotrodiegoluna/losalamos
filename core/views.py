from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages #envia mensajes
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm, PacienteForm # formulario personalizado (validacion de errores)
from crispy_forms.helper import FormHelper
from django.core.paginator import Paginator # importar paginacion 
from django.http import Http404  # importa pagna de error

# para usar el calendario
import calendar
from django.views import View

from core.models import Event
from django import forms
#from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput

from .models import Event,Paciente

import logging
logger = logging.getLogger('django')


#Importaciones para las vistas de reserva

from core.models import Medico, Especialidad, TipoServicio,Servicio,Event,ReservaHora



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
 
def paciente(request):
    pacientes = Paciente.objects.all()
    cantidad_total = Paciente.objects.count()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(pacientes, 2)
        pacientes = paginator.page(page)

    except:
        raise Http404 #pagina de error

    data = {
        'pacientes': pacientes,
        'cantidad_total':cantidad_total,
        'paginator': paginator,
    }
    return render(request,'core/Paciente.html',data)
def nuevo_paciente(request):
    data = {
        'formulario_agregar': PacienteForm
    }

    if request.method == 'POST':
        formulario = PacienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado correctamente")
            data["mensaje"] = "Guardado con exito"
            return redirect(to="productos")
        else: 
            data["formulario_agregar"] = formulario
    return  render(request,'core/nuevo-paciente.html',data)