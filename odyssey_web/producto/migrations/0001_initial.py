# Generated by Django 4.0.4 on 2022-05-21 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=12, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=70)),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField(null=True)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.categoria')),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.proveedor')),
            ],
        ),
    ]
