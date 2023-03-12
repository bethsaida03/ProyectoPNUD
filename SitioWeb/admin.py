from django.contrib import admin
from .models import *

admin.site.register(Producto)
admin.site.register(Orden)
admin.site.register(OrdenItem)
admin.site.register(Usuario)
