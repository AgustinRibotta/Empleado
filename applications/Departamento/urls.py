from .views import *
from django.urls import path

app_name = "departamento_app"

urlpatterns = [
    path(
        'new-departamento/', 
        NewDepartamentoView.as_view(), 
        name='newdep'
    ),
    path(
        'lista-departamento/',
         DepartamentoListView.as_view(),
          name='lista'
    ),

]
