from django.contrib import admin
from .models import Producto, Categoria, Cliente, Contacto

# Register your models here.

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Contacto)
