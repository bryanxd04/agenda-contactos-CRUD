from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/nuevo/', views.contacto_create, name='contacto_create'),
    path('contacto/editar/<int:pk>/', views.contacto_edit, name='contacto_edit'),
    path('contacto/eliminar/<int:pk>/', views.contacto_delete, name='contacto_delete'),
]