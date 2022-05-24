# Generated by Django 4.0.4 on 2022-05-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_imagenlogo_titulo_presentacion1_titulo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentacion3',
            fields=[
                ('id_presentacion', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=20)),
                ('descripcion', models.TextField(max_length=310)),
                ('imagen', models.ImageField(null=True, upload_to='logo')),
            ],
        ),
        migrations.DeleteModel(
            name='imagenLogo',
        ),
    ]