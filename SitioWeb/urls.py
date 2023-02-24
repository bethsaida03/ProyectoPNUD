from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Home, name='home'),
    path('', views.carrito, name='carrito')
]