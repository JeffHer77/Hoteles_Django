from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def products(request):
    return render(request, "products.html")

def events(request):
    return render(request, "events.html")

def precios(request):
    return render(request, "precios.html")

def restaurants(request):
    return render(request, "restaurants.html")

def cust_serv(request):
    return render(request, "custServ.html")


