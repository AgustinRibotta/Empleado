from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (DetailView,ListView,DeleteView,CreateView,TemplateView,UpdateView)

from .models import Empleado
from .forms import EmpleadoForm

class InicioView(TemplateView):
    # Carga pagina de incio.
    template_name = 'inicio.html'


# Create your views here.

class ListAllEmpleados(ListView):
    # Lista de empleados.
    template_name = 'Persona/lista_all.html'
    # De esta manera realizas paginacion.
    paginate_by = 4
    ordering = 'first_name'
    context_object_name ='allempleados'

    # Esto nos permite filtrar de la base de datos. icontain =  contiene.
    # Como en este caso es un vacio te va a devolver toda la base de
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )
        return lista



##### CRUD #########

    
# Liste de empleados de un area.

class ListAreEmpleados(ListView):
    template_name = 'Persona/lista_area.html'
    context_object_name = 'empleados'
    # Forma no obtima.
    # queryset = Empleado.objects.filter(
    #     departamento__shor_name = 'Otro'
    # )
    def get_queryset(self):
        # Recuperamos el dato que carga en la urel.
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
        )   
        return lista

# Lista de empleados por trabajos.

class ListJobEmpleados(ListView):
    # Liste de empleados de un area.
    template_name = 'Persona/lista_job.html'
    # Forma no obtima.
    # queryset = Empleado.objects.filter(
    #     departamento__shor_name = 'Otro'
    # )

    def get_queryset(self):
        # Recuperamos el dato que carga en la url.
        trabajo = self.kwargs['name']

        lista = Empleado.objects.filter(
        job = trabajo
        )
        return lista

    context_object_name= 'hola'

# Lista empelados por palabra calve.

class ListEmpleadosByKword(ListView):
    template_name = 'Persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
        first_name = palabra_clave
        )
        return lista

# Lista de habilidades.

class ListHAbEmpleado(ListView):
    template_name = 'Persona/habilidades.html'
    context_object_name = 'habilid'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')

        try:
            empleado = Empleado.objects.get(first_name = palabra_clave)
            
            return empleado.habilidades.all()

        except:
            return


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "Persona/detail.html"

        
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        # Todo un proceso.
        context['titulo'] = 'Empelado del mes'

        return context


class SuccesView(TemplateView):
    template_name = "Persona/succes.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "Persona/add.html"
    # fields = ('__all__') 
    form_class = EmpleadoForm
    #Si se trabaja con formularios no se neccitan los fielsd
    # fields = ['first_name',
    #     'last_name',
    #     'job',
    #     'departamento',
    #     'habilidades',
    #     'image',
    # ]
    # success_url = '/succes'
    success_url = reverse_lazy ('persona_app:empleados_admi')

    # interceptar datos.
    # Full name.

    def form_valid(self,form ):
        # Crea una instancia para poder modificar. 
        empleado = form.save(commit = False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        # Realia guardado.
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "Persona/update.html"
    fields = ['first_name',
    'last_name',
    'job',
    'departamento',
    'habilidades',
    'image',
]
    success_url = reverse_lazy ('persona_app:empleados_admi')

# Estos dos metodos funcionan tando en el Create como Update.
# Se interseptan datos antes de validarlos.

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('********** METODO POST  *********')
        print('********** METODO POST  *********')
        # ruquest.POST genera un diccionario con los daots.
        print(request.POST)
        # Utilisamos la key para llmar el value.
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    # se interseptan datos despues de validadrlos.

    def form_valid(self,form ):
        print('********** METODO form valid *********')
        print('********** METODO form valid *********')

        return super(EmpleadoUpdateView, self).form_valid(form)


# Para delete te solicita un template para confirmacion de la eliminacion.
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "Persona/delete.html"
    success_url = reverse_lazy ('persona_app:empleados_admi')


class ListaEmpleadosAdminView(ListView):
    # Lista de empleados.
    template_name = 'Persona/lista_empleados.html'
    # De esta manera realizas paginacion.
    paginate_by = 10
    ordering = 'first_name'
    context_object_name ='empleados'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )
        return lista

