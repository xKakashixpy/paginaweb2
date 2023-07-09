from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.nombre} ->{self.precio}'
    
class Cliente(models.Model):
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellidos}'
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre} - {self.correo}'    