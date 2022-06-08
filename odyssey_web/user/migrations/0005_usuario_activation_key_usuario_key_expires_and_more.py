# Generated by Django 4.0.4 on 2022-06-06 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_merge_20220531_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='activation_key',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AddField(
            model_name='usuario',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2022, 6, 6)),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=60, unique=True, verbose_name='Correo'),
        ),
    ]