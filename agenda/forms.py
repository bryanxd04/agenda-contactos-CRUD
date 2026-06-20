from django import forms
from django.forms import inlineformset_factory
from .models import Contacto, Direccion, Telefono

# Formulario para Contacto
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'apellidos', 'fotografia', 'fecha_nacio']
        widgets = {
            'fecha_nacio': forms.DateInput(attrs={'type': 'date'}),
        }

# Formulario para Dirección
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero_exterior', 'numero_interior', 'colonia', 'municipio', 'estado', 'referencias']
        widgets = {
            'estado': forms.Select(choices=Direccion._meta.get_field('estado').choices),
        }

# Formset para Teléfonos (permite agregar múltiples teléfonos)
TelefonoFormSet = inlineformset_factory(
    Contacto,
    Telefono,
    fields=['tipo', 'alias', 'numero'],
    extra=1,
    can_delete=True
)