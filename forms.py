from django import forms
from feriavirtual.models import Usuario


class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre1', 'nombre2', 'appaterno', 'apmaterno', 'correo',]

        labels = {
            'nombre1': 'Primer Nombre',
            'nombre2': 'Segundo Nombre',
            'appaterno': 'Apellido Materno',
            'apmaterno': 'Apellido Paterno',
            'correo': 'Correo Electronico',
        }

class FormularioCrearUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rutopasaporte', 'dv', 'nombre1', 'nombre2', 'appaterno', 'apmaterno', 'correo','contrasenia',]

        labels = {
            'rutopasaporte': 'Rut o Pasaporte',
            'dv': 'Digito',
            'nombre1': 'Primer Nombre',
            'nombre2': 'Segundo Nombre',
            'appaterno': 'Apellido Materno',
            'apmaterno': 'Apellido Paterno',
            'correo': 'Correo Electronico',
            'contrasenia' : 'Contraseña',
        }