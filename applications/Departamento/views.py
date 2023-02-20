from django.shortcuts import render
from .forms import *
from django.views.generic.edit import FormView
from applications.Persona.models import Empleado
from django.views.generic import ListView
from .models import Departamento
# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "Departamentos/lista.html"
    context_object_name = 'departamento'


class NewDepartamentoView(FormView):
    template_name = 'Departamentos/new.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        print ('******* Estamos en form valid****')

        # Instancia del modelo departamento.

        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname'],
        )
        depa.save()

        name = form.cleaned_data['nombre']
        apellido =form.cleaned_data['nombre']
        Empleado.objects.create(
            first_name = name,
            last_name = apellido,
            departamento = depa,
        )
        return super(NewDepartamentoView,self).form_valid(form)