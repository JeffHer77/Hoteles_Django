from django.db import models
from django.core.validators import RegexValidator

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(
        max_length=20,  # Ajusta la longitud según tus necesidades
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{7,15}$',  # Expresión regular para validar números de teléfono
                message="Número de teléfono inválido. Usa un formato como '+1234567890'."
            )
        ],
        blank=True,  # Si el campo es opcional
    )
    email = models.EmailField(unique=True)
    # Otros campos

class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    tipo_producto = models.CharField(max_length=255,blank=False)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    telefono = models.CharField(
        max_length=20,  # Ajusta la longitud según tus necesidades
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{7,15}$',  # Expresión regular para validar números de teléfono
                message="Número de teléfono inválido. Usa un formato como '+1234567890'."
            )
        ],
        blank=True,  # Si el campo es opcional
    )
    descripcion = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Cliente(models.Model):
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    celular = telefono = models.CharField(
        max_length=20,  # Ajusta la longitud según tus necesidades
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{10,18}$',  # Expresión regular para validar números de teléfono
                message="Número de teléfono inválido. Usa un formato como '+11234567890'."
            )
        ],
        blank=True,  # Si el campo es opcional
    )
    email = models.EmailField(unique=True)
    # Otros campos

class Tarjeta(models.Model):
    numero_tarjeta = models.CharField(max_length=16)
    mes_venc = models.CharField(max_length=2, null= False)
    anio_venc = models.CharField(max_length=2, null= False)
    cliente_tar = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class HistorialCompra(models.Model):
    cliente_hist = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.SET_NULL, null=True)
    fecha_compra = models.DateTimeField()

class Compras_Productos(models.Model):
    compra = models.ForeignKey(HistorialCompra, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length= 10, null=False)
    medio_pago = models.CharField(max_length=20, null= False)