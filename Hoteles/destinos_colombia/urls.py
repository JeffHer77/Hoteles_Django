from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.products, name="products"),
    path("custServ", views.custServ, name="custServ"),
    path("events", views.events, name="events"),
    path("precios", views.precios, name="precios"),
    path("restaurants", views.restaurants, name="restaurants"),
    path("clientes", views.clientes, name="clientes"),
    path("datos", views.datos, name="datos"),
    path("eliminarClientes", views.eliminarClientes, name="eliminarClientes"),


]