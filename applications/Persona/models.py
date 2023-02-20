from django.db import models
from applications.Departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad 

    
class Empleado (models.Model):
    # Modelo para table emoleado

    JOB_CHOICES = {
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('3', 'ECONOMISTA'),
        ('4', 'OTRO'),
    }
    # contador
    # Admin
    # Economista
    # Otros
    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    full_name = models.CharField('Nombre Completo', max_length=120, blank= True)
    job = models.CharField('Trabajo',max_length=1, choices= JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='empleado',blank= True, null= True)
    habilidades = models.ManyToManyField(Habilidades)
    # App de terceros.
    hoja_vida = RichTextField(blank=True)
    
    class Meta:
        verbose_name = 'Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name    