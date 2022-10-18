from django import forms
from Blog.models import *

# Formulario de Preguntas
class PreguntaForm(forms.ModelForm):
  class Meta:
    model = Pregunta
    fields = '__all__'