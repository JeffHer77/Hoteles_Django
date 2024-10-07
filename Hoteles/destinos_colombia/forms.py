from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Cliente, Empresa

class ClienteCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    celular = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ('email', 'user_type', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Cliente.objects.create(user=user, first_name=self.cleaned_data['first_name'],
                                    last_name=self.cleaned_data['last_name'],
                                    celular=self.cleaned_data['celular'])
        return user

class EmpresaCreationForm(UserCreationForm):

    nombre = forms.CharField(max_length=255)
    direccion = forms.CharField(max_length=400, required=True)
    telefono = forms.CharField(max_length=18, required= False)

    class Meta:
        model = CustomUser
        fields = ('email', 'nombre', 'user_type', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Empresa.objects.create(user=user, nombre=self.cleaned_data['nombre'],
                                    direccion=self.cleaned_data['direccion'],
                                    telefono= self.cleaned_data['telefono'])
        return user

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.CharField(label='Email', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)