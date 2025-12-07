from django.shortcuts import render
from .models import Paciente

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, "lista_pacientes.html", {"pacientes": pacientes})
