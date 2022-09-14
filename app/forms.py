from cProfile import label
from dataclasses import field
from socket import fromshare
from tkinter.ttk import Widget
from django import forms
from .models import AsesoriaEspecial
from django.utils.translation import gettext_lazy as _

class AsesoriasForm(forms.ModelForm):
    asesoriafecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    
    class Meta:
        model = AsesoriaEspecial
        fields = 'razonsolicitud' , 'asesoriafecha' , 'fechasolicitud' , 'descripcion'
        labels = {
            'razonsolicitud': _('Razon Solicitud '),
            'asesoriafecha': _('Fecha Asesoria '),
            'descripcion': _('Descripcion ')

        }
        