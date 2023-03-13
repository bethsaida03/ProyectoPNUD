from django.urls import path
from . import views
from .views import *
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Home, name='home'),
    path('carrito', views.carrito, name='carrito'),
    path('registro', views.registro, name='registro'),
    path('iniciosesion', views.iniciosesion, name='iniciosesion'),
    path('piedepagina', views.piedepagina, name='piedepagina'),
    path('producto', views.producto, name='producto'),
    path('update_item', views.updateItem, name="update_item")
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)