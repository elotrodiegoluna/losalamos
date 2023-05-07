from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages #envia mensajes
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


def home(request):   #pagina de inicio
    return render (request, 'home.html')


def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request, f"Bienvenid@ de nuevo {nombre_usuario}")
                return redirect("home")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")

    form = AuthenticationForm()
    return render(request,"login.html",{"form" : form})

def LogOut(request):
    logout(request)
    return redirect('/')

def registro(request):
    return render(request,'registro.html')