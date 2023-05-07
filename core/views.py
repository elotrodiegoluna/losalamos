from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages #envia mensajes
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm # formulario personalizado (validacion de errores)
from crispy_forms.helper import FormHelper


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
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

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
    return render(request,'registro.html')