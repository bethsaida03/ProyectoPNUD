from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email= models.CharField(max_length=200, null=True)

    def __str__(self) :
        return self.name
    

class Product(models.Model):

    image = models.ImageField( upload_to='productos', null=True)
    name = models.CharField(max_length=150, )
    price = models.IntegerField()
   
    
    class Meta:
       
        verbose_name_plural = "Producto"

    def __str__(self):
        return f' {self.name}'

    @property
    def imageURL(self):
        try: 
            url =self.image.url
        except: 
            url =''
        return url

class Order (models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    transaccion_id = models.CharField(max_length=200, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total =sum([item.get_total for item in orderitems])
        return total
    
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total =sum([item.quantity for item in orderitems])
        return total

class OrderItem (models.Model):  
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity =models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    
# Create your models here.

    
    
