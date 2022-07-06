from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    precio = models.IntegerField()
    existencia =models.IntegerField(default = 0)
    imagen = models.ImageField(upload_to='images/')
    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    total = models.FloatField(default=0)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    clientes = models.ManyToManyField(Producto)
    def __str__(self):
        return "ID: [{0}], Nombre: {1}, Total: {2}".format(self.id,self.nombre,self.totalo)