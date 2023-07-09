from django.shortcuts import render, redirect
from core.models import Producto
from core.Carrito import Carrito


# Create your views here.

def home(request):
    return render(request,'core/home.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'core/tienda.html', {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('tienda')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect('tienda')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('tienda')


def misionyvision(request):
    return render(request, 'core/misionyvision.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def noticias(request):
    return render(request, 'core/noticias.html')

def carrito(request):
    return render(request, 'core/carrito.html')

