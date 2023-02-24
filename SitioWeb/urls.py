from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Home, name='home'),
    path('carrito', views.carrito, name='carrito')
]