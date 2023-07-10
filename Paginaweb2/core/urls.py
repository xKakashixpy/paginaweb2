from django.contrib import admin
from django.urls import path
from .views import home, tienda, misionyvision, servicios, noticias, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, producto_crud, registrarproducto, eliminarproducto,editarproducto, editarproducto2

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
]
