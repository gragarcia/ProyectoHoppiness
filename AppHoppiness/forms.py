from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BebidaFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(error_messages={'required': 'Por favor ingrese un nombre'})
    categoria = forms.CharField(error_messages={'required': 'Por favor ingrese una categoria (cerveza, etc)'})
    estilo = forms.CharField(required=False)
    ibu = forms.FloatField(required=False)
    marca = forms.CharField(required=False)
    porcentaje_alcohol = forms.FloatField(required=False, max_value=100, min_value=0.0)
    precio_regular = forms.FloatField( max_value=10000, min_value=0.0)
    precio_happy_hour = forms.FloatField(max_value=10000, min_value=0.0)
    volumen = forms.CharField(required=False)
    imagen = forms.URLField(required=False)

class ComidaFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(error_messages={'required': 'Por favor ingrese un nombre'}, max_length=50, help_text='50 caracters max.')
    descripcion = forms.CharField(error_messages={'required': 'Por favor ingrese una descripción: delivery o casero, etc'}, max_length=50, help_text='50 caracters max.')
    precio_regular = forms.FloatField(max_value=10000, min_value=0.0)
    precio_happy_hour = forms.FloatField(max_value=10000, min_value=0.0)
    foto = forms.URLField(required=False)
    
class EventoFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField()
    descripcion = forms.CharField()
    fecha = forms.DateField()
    horario = forms.CharField()       
    
class ValoracionFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(error_messages={'required': 'Por favor ingrese un nombre'}, max_length=50, help_text='50 caracters max.')
    apellido = forms.CharField(error_messages={'required': 'Por favor ingrese el apellido'}, max_length=50, help_text='50 caracters max.')
    opinion = forms.CharField(error_messages={'required': 'Por favor ingrese su valoración'}, max_length=50, help_text='500 caracters max.')
    fecha = forms.DateField()
    estrellas = forms.IntegerField()

class UserFormulario(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields = ['username', 'email', 'password1', 'password2']
        
        