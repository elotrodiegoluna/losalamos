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
from .models import User

import logging
logger = logging.getLogger('django')

#libreria send mail
from django.core.mail import send_mail
from django.conf import settings


#Importaciones para las vistas de reserva

from core.models import Medico, Especialidad, TipoServicio,Servicio,Event,ReservaHora


def home(request):   #pagina de inicio
    context = {}

    if 'login_success' in request.session:
        context['show_modal'] = True
        del request.session['login_success'] # Eliminar variable
    return render (request, 'home.html', context)

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
                request.session['login_success'] = True  # Variable en la sesión del usuario
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
            user = authenticate(email=email, password=raw_password)
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


# RECUPERAR CONTRASEÑA #

import uuid
def resetpassword(request):
    context = {}
    if request.POST:
        email = request.POST['email']
        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            user_obj = User.objects.get(email=email)
            token = str(uuid.uuid4())
            user_obj.token_recuperarpass = token
            user_obj.save()
            send_forget_password_mail(email, token)
            # correo enviado
            return render(request, 'resetpassword_request.html')
        context = {
            'user_exists': email
        }
    return render(request, 'resetpassword.html', context)

def resetpassword_request(request):
    print(request.session["recover_email"])
    return render(request, 'resetpassword_request.html')

def resetpassword_reset(request, token):
    print(token)
    context = {}

    try:
        user_obj = User.objects.filter(token_recuperarpass = token).first()
        print(user_obj)
        context = {'user_id': user_obj.id}
        print(user_obj.id)
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.success(request, 'ningun id encontrado')
                return redirect(f'/change-password/{token}/')
            if new_password != confirm_password:
                messages.success(request, 'las contraseñas no coinciden')
                return redirect(f'/change-password/{token}/')

            #user_obj = User.objects.get(id = user_id)
            print(user_obj)
            context = {'user_id': user_obj.id}
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('acceder')
        
    except Exception as e:
        print(e)
    return render(request, 'resetpassword_reset.html')

def send_forget_password_mail(email, token):
    subject = 'Enlace de recuperación de contraseña'
    message = f'Hola, haz click en el enlace para reestablecer tu contraseña. http://localhost:8000/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True