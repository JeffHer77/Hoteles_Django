from tkinter import Entry

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ClienteForm
from .models import Cliente

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

def custServ(request):
    return render(request, "custServ.html")

def clientes(request):

    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():

            nombres = form.cleaned_data['cliente_nombre']
            apellidos = form.cleaned_data['cliente_apellido']
            celular = form.cleaned_data['celular']
            email = form.cleaned_data['celular']
            cliente = Cliente(nombres=nombres, apellidos=apellidos, celular= celular, email=email)
            cliente.save()

    else:
        form = ClienteForm()

    return render(request, "clientes.html", {'form': form })


def eliminarClientes(request):

    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():

            num = get_object_or_404(Cliente, celular=form.cleaned_data['celular'])

            num.delete()
            return redirect('/datos')

def datos(request):
    modelo = Cliente.objects.all()
    return render(request, 'datos.html', {'clientes': modelo})

