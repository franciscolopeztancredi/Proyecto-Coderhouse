from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Avatar(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

  def __str__(self):
    return f"Avatar de {self.usuario}"

class Mensajes(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  fecha = models.DateTimeField(auto_now_add=True)
  mensaje = models.TextField()
  numero = models.IntegerField(null=True)

  class Meta:
    verbose_name_plural = "Mensajes"
  
  def __str__(self):
    return f"{self.usuario}: {self.mensaje}"