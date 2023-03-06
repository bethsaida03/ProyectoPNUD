from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    imagen = models.ImageField( upload_to='productos', null=True)
    nombre = models.CharField(max_length=150, )
    descripcion = models.TextField(max_length=150, )
    valor = models.IntegerField()
    date_create = models.DateTimeField(auto_now=True)
    
    class Meta:
       
        verbose_name_plural = "Producto"

    def __str__(self):
        return f' {self.nombre}, ${self.valor}-producto'


class Orden (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad =models.IntegerField(default=0, null=True, blank=True)
    dato_agred = models.DateTimeField(auto_now_add=True)
