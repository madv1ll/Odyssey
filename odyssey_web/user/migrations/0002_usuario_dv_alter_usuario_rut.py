# Generated by Django 4.0.4 on 2022-05-31 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='dv',
            field=models.CharField(default='1', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
