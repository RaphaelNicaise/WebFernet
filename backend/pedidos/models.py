from django.db import models
from django.conf import settings

from carritos.models import Cart
from productos.models import Producto

# Create your models here.
class Pedido(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    carrito = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido,related_name='items',on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()