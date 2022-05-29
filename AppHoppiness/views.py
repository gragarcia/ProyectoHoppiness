from pyclbr import Class
from django.http import HttpResponse
from django.shortcuts import render
from AppHoppiness.forms import BebidaFormulario, EventoFormulario, UserFormulario
from AppHoppiness.models import Bebida, Comida, Evento, Valoracion
from django.template import loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def inicio(request):
    
    return render(request, "AppHoppiness/inicio.html" ) 

# LOGIN
def login_request(request):
    if request.method == 'POST': #al presionar el botón Login
        
        #Leer la data del formulario de inicio de sesión
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password= contra)

            if user: # si se encuentra un user con esos datos
                login(request, user) #hace el login
                
                #se muestra la página de inicio con un mensaje de bienvenida
                return render(request, "AppHoppiness/inicio.html", {"mensaje": f"Bienvenido {user}"})

        else: 
            # si el formulario no es valido mostramos la pagina de inicio y un mensaje de error 
            return render(request, "AppHoppiness/inicio.html", {"mensaje": "Error. Los datos ingresados son incorrectos"})

    else: 
        form = AuthenticationForm()
        
    return render(request, "AppHoppiness/login.html", {'form': form})

#REGISTER
def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user_name= form.cleaned_data['username']
            form.save()
            
            return render(request, "AppHoppiness/inicio.html", {"mensaje": "Usuario creado :) "})
    else: 
        form = UserCreationForm()
    
    return render(request, "AppHoppiness/registro.html", {"form": form})
    
@login_required    
def editarUsuario(request):
    usuario = request.user #usuario que ha iniciado sesion
    
    if request.method == 'POST':
        
        miFormulario = UserFormulario(request.POST)
        
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data
            
            #actualizar info del usuario activo
            usuario.username = info['username']
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            
            usuario.save()
            
            return render(request, "AppHoppiness/inicio.html")
    else: 
         miFormulario = UserFormulario(initial={'username': usuario.username, 
                                       'email': usuario.email})
         
    return render(request, "AppHoppiness/editarUsuario.html", {'miFormulario': miFormulario, 'usuario': usuario.username })
            
        
def about(request):
    
    return render(request, "AppHoppiness/about.html" )        
    
    
# Bebida
def bebida(request):
    
    return render(request, "AppHoppiness/Bebidas/bebidas.html" )   

class BebidaLista(LoginRequiredMixin, ListView):
    model = Bebida
    template_name = "AppHoppiness/Bebidas/listaBebida.html"
     
class BebidaDetalle(LoginRequiredMixin, DetailView):
    model = Bebida
    template_name = "AppHoppiness/Bebidas/bebidaDetalle.html"

class BebidaCreacion(LoginRequiredMixin, CreateView):
    model = Bebida
    success_url = "/AppHoppiness/bebidas/lista"
    fields = ['nombre', 'categoria', 'estilo', 'ibu', 'marca', 'porcentaje_alcohol', 'precio_regular', 'precio_happy_hour', 'volumen', 'imagen']

class BebidaEdicion(LoginRequiredMixin, UpdateView):
    model = Bebida
    success_url = "/AppHoppiness/bebidas/lista"
    fields = ['nombre', 'categoria', 'estilo', 'ibu', 'marca', 'porcentaje_alcohol', 'precio_regular', 'precio_happy_hour', 'volumen', 'imagen']

class BorrarBebida(LoginRequiredMixin, DeleteView):
    model = Bebida
    success_url = "/AppHoppiness/bebidas/lista"
        
    
# Comida     
def comida(request):
    
    return render(request, "AppHoppiness/Comidas/comidas.html" )   

class ComidaLista(LoginRequiredMixin, ListView):
    model = Comida
    template_name = "AppHoppiness/Comidas/listaComida.html"
     
class ComidaDetalle(LoginRequiredMixin, DetailView):
    model = Comida
    template_name = "AppHoppiness/Comidas/comidaDetalle.html"

class ComidaCreacion(LoginRequiredMixin, CreateView):
    model = Comida
    success_url = "/AppHoppiness/comidas/lista"
    fields = ['nombre', 'descripcion', 'precio_regular', 'precio_happy_hour', 'foto']

class ComidaEdicion(LoginRequiredMixin, UpdateView):
    model = Comida
    success_url = "/AppHoppiness/comidas/lista"
    fields = ['nombre', 'descripcion', 'precio_regular', 'precio_happy_hour', 'foto']

class BorrarComida(LoginRequiredMixin, DeleteView):
    model = Comida
    success_url = "/AppHoppiness/comidas/lista"



# Promos 
def promo(request):
    return render(request, "AppHoppiness/Promos/promos.html" )  

# Eventos 
def evento(request):
    return render(request, "AppHoppiness/Eventos/eventos.html" )   

# Valoraciones
class ValoracionLista(ListView):
    model = Valoracion
    template_name = "AppHoppiness/Valoraciones/listaValoracion.html" 