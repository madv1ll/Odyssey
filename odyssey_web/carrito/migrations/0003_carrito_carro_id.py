# Generated by Django 4.0.4 on 2022-05-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='carro_id',
            field=models.CharField(default='', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
