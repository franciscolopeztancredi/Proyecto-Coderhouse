from django import forms
from Post.models import *

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