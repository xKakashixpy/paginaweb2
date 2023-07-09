from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.nombre} ->{self.precio}'