from django.db import models
from django.contrib.auth.models import User

# Clase Post: Publicaciones dentro de mi blog
class Post(models.Model):

  titulo = models.CharField(max_length=50)
  fecha = models.DateField()
  autor = models.CharField(max_length=20)
  image = models.URLField()
  texto = models.TextField()
  num_entrada = models.IntegerField()

  def __str__(self):
    return f"{self.fecha}, {self.titulo}"



# Clase Comentario: Comentarios dentro de cada post
class Comentario(models.Model):

  nombre = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  comentario = models.TextField()
  fecha = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name="comentarios")

  def __str__(self):
    return f"[{self.post.titulo}] {self.comentario}"