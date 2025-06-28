from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10000, decimal_places=2)
    image = models.ImageField(upload_to='productos/', null=True, blank=True)
    disponible = models.BooleanField(default=True)