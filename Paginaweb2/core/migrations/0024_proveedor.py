# Generated by Django 4.2.2 on 2023-07-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_delete_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]
