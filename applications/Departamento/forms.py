from django import forms

class NewDepartamentoForm(forms.Form):
    """NewDepartamento definition."""
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=30)

    # TODO: Define form fields here
