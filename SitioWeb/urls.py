from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.Home, name='home'),
    path('carrito', views.carrito, name='carrito'),
    path('registro', views.registro, name='registro'),
    path('iniciosesion', views.iniciosesion, name='iniciosesion'),
    path('piedepagina', views.piedepagina, name='piedepagina'),path('producto', views.producto, name='producto'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Dub"),
    path('limpiar/', limpiar_carrito, name="CLS"), 
    path('Carrito_compra', views.Carrito_compra, name='Carrito_compra'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)