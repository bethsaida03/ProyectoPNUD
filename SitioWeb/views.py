from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView 
from django.template import loader
from contextlib import _RedirectStream
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm,  UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import JsonResponse,  HttpResponse
import json
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
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =Order.objects.get_or_create( customer= customer)
        items = order.orderitem_set.all()
       
    else:
        items = []
        order = {'get_cart_total':0, 'get_cartitems':0 }
      

    context={'items': items, 'order':order}
    return render(request, 'SitioWeb/carrito.html', context)

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
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created =Order.objects.get_or_create( customer= customer)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
       
    else:
        items = []
        order = {'get_cart_total':0, 'get_cartitems':0 }
        
      

     
    products = Product.objects.all()
    context = {'products': products,  'order':order}
    return render(request, 'SitioWeb/producto1.html', context )


def limpiar_carrito(request, producto_id):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('producto')

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created =Order.objects.get_or_create(customer=customer)

    orderItem, created =OrderItem.objects.get_or_create(order= order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


