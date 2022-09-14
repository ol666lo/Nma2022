from dataclasses import dataclass
from django.shortcuts import render, redirect
from .models import VistaClientes
from django.contrib.auth.decorators import login_required 
from .forms import AsesoriasForm
from django.contrib import messages 
# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'app/home.html')

def base(request):
    return render(request, 'app/base.html')

def solicitarasesoria(request):

    data = {
        'form': AsesoriasForm()
    }

    if request.method == 'POST':
        solicitud = AsesoriasForm(data=request.POST)
        if solicitud.is_valid():
            solicitud.save()
            messages.success(request, "Solicitud Registrada Correctamente")
            return redirect(to="home")
    return render(request, 'app/solicitarasesoria.html', data)

def verclientes(request):
    vistaClientess = VistaClientes.objects.all()
    data = { 
        'vistaClientess': vistaClientess
    }
    return render(request,'app/verclientes.html', data)  