from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)

    def _str_(self) :
        return self.name
    

class Producto(models.Model):

    imagen = models.ImageField( upload_to='productos', null=True)
    nombre = models.CharField(max_length=150, )
    valor = models.IntegerField()
    date_create = models.DateTimeField(auto_now_add=True)
    
    class Meta:
       
        verbose_name_plural = "Producto"

    def _str_(self):
        return f' {self.nombre}'


class Orden (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True)
    transaccion_id = models.CharField(max_length=200, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        ordenitems = self.ordenitem_set.all()
        total =sum([item.get_total for item in ordenitems])
        return total
    
    def get_cart_items(self):
        ordenitems = self.ordenitem_set.all()
        total =sum([item.cantidad for item in ordenitems])
        return total

class OrdenItem (models.Model):  
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(Orden, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad =models.IntegerField(default=0, null=True, blank=True)
    dato_agred = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.producto.valor * self.cantidad 
        return total
    
    
