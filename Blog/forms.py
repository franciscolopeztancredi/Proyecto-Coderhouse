from django import forms
from Blog.models import *



# Formulario de Creación de Posts
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'



# Formulario de Comentarios
class ComentarioForm(forms.ModelForm):
  class Meta:
    model = Comentario
    fields = ("nombre", "comentario")



# Formulario de Preguntas
class PreguntaForm(forms.ModelForm):
  class Meta:
    model = Pregunta
    fields = '__all__'