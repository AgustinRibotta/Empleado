from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Habilidades)

# De esta manera indicamos como vamos a ver la tabla en el administrador.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
     
    # Agregamos una nueva columna. 
    def full_name (selft, obj):
        return  obj.first_name + ' ' + obj.last_name


    # Buscador.
    search_fields = ('first_name',)

    # Filtrador.
    list_filter = ('job','habilidades','departamento')

    # Filtro.
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)