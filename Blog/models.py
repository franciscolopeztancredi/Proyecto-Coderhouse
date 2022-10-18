from django.db import models

# Clase Pregunta: Preguntas dentro de la sección Contacto
class Pregunta(models.Model):

  nombre = models.CharField(max_length=100)
  email = models.EmailField()
  telefono = models.IntegerField(blank=True)
  pregunta = models.TextField()

  def __str__(self):
    return f"{self.nombre}: {self.pregunta}"