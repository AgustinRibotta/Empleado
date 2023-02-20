from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Prueba
from applications.Persona.models import Empleado
from .forms import PruebaForm

# Create your views here.


class IndexView (TemplateView):
    template_name = 'Home/home.html'

class ResumenFundationView (TemplateView):
    template_name = 'Home/resumenFundation.html'


class PruebaListView(ListView):
    template_name = 'Home/lista.html'
    queryset = ['A', 'B', 'c']
    context_object_name = 'lista_prueba'


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "Home/prueba.html"
    context_object_name = 'lista_prueba'


class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "Home/add.html"
    form_class = PruebaForm
    success_url = '/'
