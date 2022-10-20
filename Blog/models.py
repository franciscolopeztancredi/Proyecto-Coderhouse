from django.db import models
from django.contrib.auth.models import User

# Clase Pregunta: Preguntas dentro de la sección Contacto
class Pregunta(models.Model):

  usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  telefono = models.IntegerField(blank=True, null=True)
  pregunta = models.TextField()

  def __str__(self):
    return f"{self.usuario}: {self.pregunta}"