from django.urls import path
from.views import home, tienda, misionyvision, servicios, noticias

urlpatterns=[
    path('',home,name="home"),
    path('tienda/',tienda,name="tienda"),
    path('misionyvision/',misionyvision,name="misionyvision"),
    path('servicios/',servicios,name="servicios"),
    path('noticias/',noticias, name="noticias"),

]