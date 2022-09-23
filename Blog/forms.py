from socket import fromshare
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from Blog.models import *



# Formulario de Registro de Usuarios
class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ["username", "email", "password1", "password2"]



# Formulario de Creación de Posts
class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = '__all__'



# Formulario de Comentarios
class ComentarioForm(ModelForm):
  class Meta:
    model = Comentario
    fields = ("nombre", "comentario")



# Formulario de Preguntas
class PreguntaForm(ModelForm):
  class Meta:
    model = Pregunta
    fields = '__all__'