# Generated by Django 4.0.4 on 2022-05-10 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carrito', '0002_carrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cant_cuotas', models.IntegerField(null=True)),
                ('monto_cuotas', models.IntegerField(null=True)),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Pago',
            fields=[
                ('id_tipo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
        migrations.AddField(
            model_name='compra',
            name='id_pago_pago',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrito.tipo_pago'),
        ),
        migrations.AddField(
            model_name='compra',
            name='rut_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
