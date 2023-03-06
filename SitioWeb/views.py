from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView 
from django.template import loader
from contextlib import _RedirectStream
from .models import *
from SitioWeb.Carrito import Carrito
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import(
        LoginForm, 
        UserForm,   
      
        )

# Create your views here.
# class Home(ListView): 
#     #para la vista 'home'
#     template_name = 'SitioWeb/home.html'

@login_required(login_url="iniciosesion") 
def Home(request):
    return render(request, 'SitioWeb/home.html', {})

def carrito(request):
    productos = Producto.objects.all()
    
    return render(request, 'SitioWeb/carrito.html', {'productos':productos})

#--------------------------REGISTRO---------------------#
def registro(request):
    msg     = None
    success = False

    if request.method == "POST":
        dat=""
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

                
            
            

            msg     = 'Usuario Creado - Por favor Ingresa <a href="SitioWeb/iniciosesion">iniciosecion</a>.'
            success = True
            
            return redirect("iniciosesion")

        else:
            msg = 'Por favor digite bien los datos'    
    else:
        form = UserForm()
        
    return render(request, 'SitioWeb/registro.html', {"form": form, "msg" : msg , "success" : success })


#--------------------------LOGIN---------------------#
def iniciosesion(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:    
                msg = 'Credenciales invalidas'    
        else:
            msg = 'Error'    
        
    return render(request, 'SitioWeb/iniciosesion.html', {"msg": msg, "form": form})

def piedepagina(request):
    return render(request, 'SitioWeb/piedepagina.html', {})




def producto(request):
    productos = Producto.objects.all()
    return render(request, 'SitioWeb/producto1.html', {'productos':productos})

def agregar_producto (request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('producto')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('producto')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('producto')

def limpiar_carrito(request, producto_id):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('producto')