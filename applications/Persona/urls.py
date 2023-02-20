from .views import *
from django.urls import path


app_name ="persona_app"

urlpatterns = [
    path(
        '',
        InicioView.as_view(),
         name='inicio'
    ),
    path(
        'lista-all/',
        ListAllEmpleados.as_view(),
         name = 'EmpleadosAll'
    ),
    path(
        'lista-area/<shorname>/',
        ListAreEmpleados.as_view(),
        name = 'empleados_area'
    ),
        path(
        'lista-empleados/',
        ListaEmpleadosAdminView.as_view(),
        name = 'empleados_admi'
    ),
    path(
        'lista-job/<name>/',
        ListJobEmpleados.as_view()
    ),
    path(
        'buscar-empleado/',
        ListEmpleadosByKword.as_view()
    ),
    path(
        'buscar-habilidades/',
        ListHAbEmpleado.as_view()
    ),
    path(
        'detail/<pk>/',
        EmpleadoDetailView.as_view(),
        name='empleado_detail'
    ),
    path(
        'addpersona/',
        EmpleadoCreateView.as_view(),
        name='empleado_add'
    ),
    path(
        'succes/',
        SuccesView.as_view(),
         name='succes'
    ),
    path(
        'update/<pk>',
        EmpleadoUpdateView.as_view(),
         name='update'
    ),
    path(
        'delete/<pk>',
        EmpleadoDeleteView.as_view(),
         name='delete'
    ),

]
