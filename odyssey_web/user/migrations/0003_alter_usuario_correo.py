# Generated by Django 4.0.4 on 2022-05-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usuario_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=60, unique=True, verbose_name='Correo'),
        ),
    ]
