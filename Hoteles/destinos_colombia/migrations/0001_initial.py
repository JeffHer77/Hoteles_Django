# Generated by Django 5.1 on 2024-10-03 00:28

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_type', models.CharField(choices=[('cliente', 'Cliente'), ('empresa', 'Empresa')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message="Número de teléfono inválido. Usa un formato como '+11234567890'.", regex='^\\+?1?\\d{10,18}$')])),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, null=True)),
                ('direccion', models.CharField(blank=True, max_length=400)),
                ('telefono', models.CharField(max_length=18)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField()),
                ('cliente_hist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos_colombia.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Compras_Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=10)),
                ('medio_pago', models.CharField(max_length=20)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos_colombia.historialcompra')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo_producto', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('telefono', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(message="Número de teléfono inválido. Usa un formato como '+1234567890'.", regex='^\\+?1?\\d{7,15}$')])),
                ('descripcion', models.CharField(max_length=255)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos_colombia.empresa')),
            ],
        ),
        migrations.AddField(
            model_name='historialcompra',
            name='servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='destinos_colombia.servicio'),
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.CharField(max_length=16)),
                ('mes_venc', models.CharField(max_length=2)),
                ('anio_venc', models.CharField(max_length=2)),
                ('cliente_tar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinos_colombia.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='historialcompra',
            name='tarjeta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='destinos_colombia.tarjeta'),
        ),
    ]
