from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nuevo/", views.nuevo_paciente, name="nuevo"),
    path("editar/<int:id>/", views.editar_paciente, name="editar_paciente"),
    path("eliminar/<int:id>/", views.eliminar_paciente, name="eliminar_paciente"),
]
