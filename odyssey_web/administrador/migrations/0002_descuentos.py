# Generated by Django 4.0.4 on 2022-05-22 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='descuentos',
            fields=[
                ('id_descuento', models.AutoField(primary_key=True, serialize=False)),
                ('pregunta', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
