# Generated by Django 4.0.4 on 2022-05-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_presentacion1_ubicacion_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentacion2',
            name='ubicacion_img',
            field=models.CharField(default='Derecha', max_length=20),
        ),
        migrations.AddField(
            model_name='presentacion3',
            name='ubicacion_img',
            field=models.CharField(default='Derecha', max_length=20),
        ),
        migrations.AlterField(
            model_name='presentacion1',
            name='ubicacion_img',
            field=models.CharField(default='Derecha', max_length=20),
        ),
    ]
