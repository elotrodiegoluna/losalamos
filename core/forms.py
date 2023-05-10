from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError
from core.models import Event
from django.contrib.auth.models import User
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Los datos no coinciden con ninguna cuenta.")



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'description']
        widgets = {
            'date': DatePickerInput(),
            
        }

