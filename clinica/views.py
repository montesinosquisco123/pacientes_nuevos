from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente

def inicio(request):
    pacientes = Paciente.objects.all()
    return render(request, "lista_pacientes.html", {"pacientes": pacientes})

def nuevo_paciente(request):
    if request.method == "POST":
        Paciente.objects.create(
            nombre=request.POST["nombre"],
            edad=request.POST["edad"],
            direccion=request.POST["direccion"],
            fecha_nacimiento=request.POST["fecha_nacimiento"],
        )
        return redirect("inicio")

    return render(request, "crear_paciente.html")

def editar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)

    if request.method == "POST":
        paciente.nombre = request.POST["nombre"]
        paciente.edad = request.POST["edad"]
        paciente.direccion = request.POST["direccion"]
        paciente.fecha_nacimiento = request.POST["fecha_nacimiento"]
        paciente.save()
        return redirect("inicio")

    return render(request, "editar_paciente.html", {"paciente": paciente})

def eliminar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    paciente.delete()
    return redirect("inicio")
