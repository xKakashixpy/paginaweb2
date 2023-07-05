from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def tienda(request):
    return render(request, 'core/tienda.html')

def misionyvision(request):
    return render(request, 'core/misionyvision.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def noticias(request):
    return render(request, 'core/noticias.html')

def carrito(request):
    return render(request, 'core/carrito.html')