from django import forms
from .models import Prueba

# Para personalizar los formulario de nuestros modelos.

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = (
        'titulo',
        'subtitulo',
        'cantidad',
        )

        # De esta manera le agrego los atributos directamente
        
        widgets = {
            'titulo' : forms.TimeInput(
                attrs = {
                    'placeholder' : 'Ingrese texto'
                }
            )

        }

    # Le ingresamos una validacion para la cantida.

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')

        if cantidad < 10:

            raise forms.ValidationError('Ingrese un numero mayor a 10')
    
         # TODO Validation
    
        return cantidad