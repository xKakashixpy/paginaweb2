from django.contrib import admin
from django.urls import path
from.views import home, tienda, misionyvision, servicios, noticias,carrito

urlpatterns=[
    path('',home,name="home"),
    path('tienda/',tienda,name="tienda"),
    path('misionyvision/',misionyvision,name="misionyvision"),
    path('servicios/',servicios,name="servicios"),
    path('noticias/',noticias, name="noticias"),
    path('carrito/', carrito,name="carrito"),   

]