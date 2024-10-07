from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=10, choices=[('cliente', 'Cliente'), ('empresa', 'Empresa')])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Empresa(models.Model):

    user = models.OneToOneField('destinos_colombia.customuser', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=255, null=True)
    direccion = models.CharField(max_length=400, blank=True)
    telefono = models.CharField( max_length=18, blank=False)


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

    user = models.OneToOneField('destinos_colombia.customuser', on_delete=models.CASCADE, null=True)
    celular = models.CharField(
        max_length=20,  # Ajusta la longitud según tus necesidades
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{10,18}$',  # Expresión regular para validar números de teléfono
                message="Número de teléfono inválido. Usa un formato como '+11234567890'."
            )
        ],
        blank=True,
    )
    first_name = models.CharField(max_length=20,  null=True)
    last_name = models.CharField(max_length=20, null=True)


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