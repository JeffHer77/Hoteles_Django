from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from pyexpat.errors import messages

from .forms import ClienteCreationForm, EmpresaCreationForm, CustomAuthenticationForm
from .models import Cliente, Empresa
from django.contrib.auth import authenticate, login, logout


def index(request):

    if request.user.is_authenticated:
        if request.user.user_type == 'cliente':
            try:
                print('entro')
                usuario = Cliente.objects.get(user=request.user)
                return render(request, "index.html", {'user': request.user, 'usuario': usuario})
            except Cliente.DoesNotExist:
                print('fallo')
                return render(request, "index.html", {'user': request.user, 'usuario': None})
        elif request.user.user_type == 'empresa':
            try:
                usuario = Empresa.objects.get(user=request.user)
                return render(request, "index.html", {'user': request.user, 'usuario': usuario})
            except Empresa.DoesNotExist:
                return render(request, "index.html", {'user': request.user, 'usuario': None})
        else:
            return render(request, "index.html", {'user': request.user, 'usuario': ''})

    else:
        return render(request, "index.html")

    return render(request, "index.html", {'user': None, 'usuario': None})

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

def datos(request):
    modelo = Cliente.objects.all()
    return render(request, 'datos.html', {'clientes': modelo})


def registroCliente(request):

    if request.method == 'POST':

        forms = ClienteCreationForm(request.POST)

        if forms.is_valid():

            forms.save()
            return redirect('/datos')

    else:
        forms = ClienteCreationForm()

    return render(request, "registroCliente.html", {'form': forms} )

def registroEmpresa(request):

    if request.method == 'POST':

        forms = EmpresaCreationForm(request.POST)

        if forms.is_valid():

            forms.save()
            return redirect('/datos')

    else:
        forms = EmpresaCreationForm()

    return render(request, "registroEmpresa.html", {'form': forms} )

def login_view(request):
    print(222222)
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print(3333333)
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Change 'home' to your desired redirect URL
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def ingreso(request):
    return render(request, 'ingreso.html')

def logoutC(request):
    logout(request)
    return redirect('/')

def salida(request):
    return render(request, 'logout.html')