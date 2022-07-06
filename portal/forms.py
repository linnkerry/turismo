from django.forms import ModelForm
from .models import Incidences

# Create the form class.
class IncidenciaForm(ModelForm):
     class Meta:
         model = Incidences
         fields = ['location', 'agente', 'agraviado', 'typeinsidence','vehiculo']