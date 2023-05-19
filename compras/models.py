from django.db import models

# Create your models here.

class Proveedor(models.Model):

    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()

    def __str__(self):
        return self.nombre
    


class Producto(models.Model):

    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 