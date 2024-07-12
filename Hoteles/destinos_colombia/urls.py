from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("products", views.products, name="products"),
    path("custServ", views.cust_serv, name="customer"),
    path("events", views.events, name="events"),
    path("precios", views.precios, name="precios"),
    path("restaurants", views.restaurants, name="restaurants"),

]