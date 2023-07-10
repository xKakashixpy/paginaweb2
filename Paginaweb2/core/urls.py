from django.contrib import admin
from django.urls import path
from.views import home, tienda, misionyvision, servicios, noticias,agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, producto_crud


urlpatterns=[
    path('',home,name="home"),
    path('tienda/',tienda,name="tienda"),
    path('misionyvision/',misionyvision,name="misionyvision"),
    path('servicios/',servicios,name="servicios"),
    path('noticias/',noticias, name="noticias"),
    path('agregar_producto/<int:producto_id>', agregar_producto, name="add"),   
    path('eliminar/<int:producto_id>', eliminar_producto,name="del"),
    path('restar/<int:producto_id>', restar_producto,name="rest"), 
    path('limpiar/', limpiar_carrito,name="empt"), 
    ## url crud
    path('ProdCrud/',producto_crud,name="producto_crud",)

]