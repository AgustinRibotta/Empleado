from django.db import models

# Create your models here.

# Blamk = True es para poder dejar un espacion en blanco.
# null = True Puede llegar a ser un valor nulo de entrada.
# Unique = True admite un valor unico no se puede repetir.
# Editable = Flase No permite editar el valor.
# Verbose_name = Nombre en la base de datos.
# Ordering Ordena por nombre.
# unique_together no puede repetir.


class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=50, unique=True)
    anulate = models.BooleanField('Anulado',default=False)

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shor_name    