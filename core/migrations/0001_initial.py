# Generated by Django 4.1.13 on 2023-12-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido1', models.CharField(max_length=100)),
                ('apellido2', models.CharField(max_length=100)),
                ('calleynumero', models.CharField(max_length=200)),
                ('cp', models.IntegerField()),
                ('localidad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
                ('fechaInicio', models.DateField()),
                ('precio', models.IntegerField()),
                ('estadoCivil', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('fechaAlta', models.DateField(auto_now=True)),
                ('fechaNacimiento', models.DateField()),
            ],
        ),
    ]