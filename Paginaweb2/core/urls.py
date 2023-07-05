from django.urls import path
from.views import home, tienda

urlpatterns=[
    path('',home,name="home"),
    path('tienda/',tienda,name="tienda",),

]