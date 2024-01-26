from django.db import models

# Create your models here.

# crear una clase por cada tabla que necesite mi base de datos
class Clientes(models.Model):
    #creacion de campos con tipo de dato y propiedad

    # se crea campo nombre con tipo de dato char
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 50)
    email = models.EmailField()
    tfno = models.CharField(max_length = 10)

class Articulos(models.Model):
    nombre = models.CharField(max_length = 30)
    seccion = models.CharField(max_length = 20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()