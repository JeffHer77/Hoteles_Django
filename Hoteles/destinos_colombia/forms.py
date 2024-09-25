from django import forms

class ClienteForm(forms.Form):

    cliente_nombre = forms.CharField(label='nombre', max_length=255)
    cliente_apellido = forms.CharField(label='apellido', max_length=255)
    celular = forms.CharField(label='celular', max_length=20)
    email = forms.EmailField(required=True, label='email')


