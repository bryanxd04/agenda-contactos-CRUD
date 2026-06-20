from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Contacto, Direccion, Telefono
from .forms import ContactoForm, DireccionForm, TelefonoFormSet

# Vista de inicio (lista de contactos)
def index(request):
    contactos = Contacto.objects.all()
    return render(request, 'index.html', {'contactos': contactos})

# Crear nuevo contacto
def contacto_create(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES)
        if form.is_valid():
            contacto = form.save()
            return redirect('contacto_edit', pk=contacto.pk)
    else:
        form = ContactoForm()
    return render(request, 'contacto_form.html', {'form': form, 'titulo': 'Crear Contacto'})

# Editar contacto (con pestañas)
def contacto_edit(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    
    # Obtener o crear dirección
    direccion, created = Direccion.objects.get_or_create(contacto=contacto)
    
    if request.method == 'POST':
        form = ContactoForm(request.POST, request.FILES, instance=contacto)
        direccion_form = DireccionForm(request.POST, instance=direccion)
        telefono_formset = TelefonoFormSet(request.POST, instance=contacto)
        
        if form.is_valid() and direccion_form.is_valid() and telefono_formset.is_valid():
            form.save()
            direccion_form.save()
            telefono_formset.save()
            return redirect('index')
    else:
        form = ContactoForm(instance=contacto)
        direccion_form = DireccionForm(instance=direccion)
        telefono_formset = TelefonoFormSet(instance=contacto)
    
    return render(request, 'contacto_edit.html', {
        'contacto': contacto,
        'form': form,
        'direccion_form': direccion_form,
        'telefono_formset': telefono_formset,
    })

# Eliminar contacto
def contacto_delete(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('index')
    return render(request, 'contacto_confirm_delete.html', {'contacto': contacto})