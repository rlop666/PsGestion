from django import forms

class AltaPaciente(forms.Form):
    dni = forms.CharField(max_length=15)
    nombre = forms.CharField(max_length=100)
    apellido1 = forms.CharField(max_length=100)
    apellido2 = forms.CharField(max_length=100)
    calleynumero = forms.CharField(max_length=200)
    cp = forms.IntegerField()
    localidad = forms.CharField(max_length=100)
    provincia = forms.CharField(max_length=100)
    fechaInicio = forms.DateField()
    precio = forms.IntegerField()
    estadoCivil = forms.CharField(max_length=50)
    email = forms.EmailField(label='Correo electrónico:',max_length=254,
                                    widget=forms.EmailInput())
    telefono = forms.CharField(max_length=20)
    fechaAlta = forms.DateField(label='Fecha de alta')
    fechaNacimiento = forms.DateField()