from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Paciente
from django.shortcuts import redirect


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='email', max_length=64)
    nombre = forms.CharField(label='nombre', max_length=64)
    rut = forms.CharField(label='rut', max_length=64)

    class Meta:
        model = Usuario
        fields = ("email", "password1", "password2", "nombre", "rut")


    


class LoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Paciente
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Los datos no coinciden con ninguna cuenta.")