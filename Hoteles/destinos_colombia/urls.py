from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.products, name="products"),
    path("custServ", views.custServ, name="custServ"),
    path("events", views.events, name="events"),
    path("precios", views.precios, name="precios"),
    path("restaurants", views.restaurants, name="restaurants"),
    path("datos", views.datos, name="datos"),
    path("registroCliente", views.registroCliente, name="registroCliente"),
    path('login', views.login_view, name='login'),
    path('ingreso', views.ingreso, name='ingreso'),
    path('logoutC', views.logoutC, name='logoutC'),
    path('salida', views.salida, name='salida'),

]