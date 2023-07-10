from django.shortcuts import render, redirect
from core.models import Producto, Categoria
from core.Carrito import Carrito

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'core/tienda.html', {'productos': productos})
## Variables del carrito de compras
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
##Cierre Varibles Carrito de Compras

def misionyvision(request):
    return render(request, 'core/misionyvision.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def noticias(request):
    return render(request, 'core/noticias.html')

def carrito(request):
    return render(request, 'core/carrito.html')


## CRUD  PRODUCTO
def producto_crud(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'core/ProdCrud.html', {"productos": productos, "categorias": categorias})

def registrarproducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    descripcion = request.POST['txtDesc']
    categoria = request.POST['txtCategoria'] 
  
    categoria = Categoria.objects.get(nombre=categoria)

    producto = Producto.objects.create(
        codigo=codigo, nombre=nombre, precio=precio, descripcion=descripcion, categoria=categoria
    )
    return redirect('producto_crud')

def editarproducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    categorias = Categoria.objects.all()  
    return render(request, "core/ProdEdit.html", {"producto": producto, "categorias": categorias})

def editarproducto2(request, codigo):
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    descripcion = request.POST['txtDesc']
    categoria = request.POST['txtCategoria']
  
    categoria = Categoria.objects.get(nombre=categoria)

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.precio = precio
    producto.descripcion = descripcion
    producto.categoria = categoria
    producto.save()

    return redirect('producto_crud')



def eliminarproducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect('producto_crud')

## CRUD  CATEGORIA    


def categoria_crud(request):
    categoria = Categoria.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'core/CatCrud.html', {"categorias": categorias, "categorias": categorias})

def registrarcategoria(request):
    nombre = request.POST['txtNombre']   

    categoria = Categoria.objects.create(
        nombre=nombre,  
    )
    return redirect('categoria_crud')

def editarcategoria(request, nombre):
    categoria = Categoria.objects.get(nombre=nombre)      
    return render(request, "core/CatEdit.html", { "categoria": categoria})

def editarcategoria2(request, nombre):
    nuevo_nombre = request.POST['txtNombre']
    categoria = Categoria.objects.get(nombre=nombre)
    categoria.nombre = nuevo_nombre
    categoria.save()
    return redirect('categoria_crud')




def eliminarcategoria(request, nombre):
    categoria = Categoria.objects.get(nombre=nombre)
    categoria.delete()

    return redirect('categoria_crud')