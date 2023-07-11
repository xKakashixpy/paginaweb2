from django.contrib import admin
from django.urls import path
from .views import home, tienda, misionyvision, servicios, noticias, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, producto_crud, registrarproducto, eliminarproducto,editarproducto, editarproducto2,categoria_crud, registrarcategoria,editarcategoria,editarcategoria2,eliminarcategoria, cliente_crud, registrarcliente, editarcliente, editarcliente2,eliminarcliente

urlpatterns = [
    path('', home, name="home"),
    path('tienda/', tienda, name="tienda"),
    path('misionyvision/', misionyvision, name="misionyvision"),
    path('servicios/', servicios, name="servicios"),
    path('noticias/', noticias, name="noticias"),
    path('agregar_producto/<int:producto_id>', agregar_producto, name="add"),   
    path('eliminar/<int:producto_id>', eliminar_producto, name="del"),
    path('restar/<int:producto_id>', restar_producto, name="rest"), 
    path('limpiar/', limpiar_carrito, name="empt"), 
    path('ProdCrud/', producto_crud, name="producto_crud"),
    path('registrarproducto/', registrarproducto, name="registrarproducto"),
    path('editarproducto/<str:codigo>/', editarproducto,name="editarproducto"),
    path('editarproducto2/<str:codigo>/', editarproducto2,name="editarproducto2"),
    path('eliminarproducto/<str:codigo>/', eliminarproducto, name="eliminarproducto" ),
    path('CatCrud/', categoria_crud, name="categoria_crud"),
    path('registrarcategoria/', registrarcategoria, name="registrarcategoria"),
    path('editarcategoria/<str:nombre>/', editarcategoria, name='editarcategoria'),
    path('editarcategoria2/<str:nombre>/', editarcategoria2,name="editarcategoria2"),
    path('eliminarcategoria/<str:nombre>/', eliminarcategoria, name="eliminarcategoria" ),
    path('ClieCrud/', cliente_crud, name="cliente_crud"),
    path('registrarcliente/', registrarcliente, name="registrarcliente"),
    path('editarcliente/<str:rut>/',editarcliente, name='editarcliente'),
    path('editarcliente2/<str:rut>/', editarcliente2,name="editarcliente2"),
    path('eliminarcliente/<str:rut>/', eliminarcliente, name="eliminarcliente" ),
]
