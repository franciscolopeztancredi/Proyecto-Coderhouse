from django.db import models
from django.contrib.auth.models import User



# Clase Tag: Tags para encontrar posts rápido
class Tag(models.Model):
  tag = models.CharField(max_length=200)

  def __str__(self):
    return self.tag



# Clase Post: Publicaciones dentro de mi blog
class Post(models.Model):

  titulo = models.CharField(max_length=50)
  fecha = models.DateField()
  autor = models.CharField(max_length=20)
  image = models.URLField()
  tags = models.ManyToManyField(Tag, blank=True)
  texto = models.TextField()
  num_entrada = models.IntegerField()

  def __str__(self):
    return f"{self.fecha}, {self.titulo}"



# Clase Comentario: Comentarios dentro de cada post
class Comentario(models.Model):

  nombre = models.CharField(max_length=100)
  comentario = models.TextField()
  fecha = models.DateTimeField(auto_now_add=True)
  post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE, related_name="comentarios")

  def __str__(self):
    return f"{self.post}, {self.nombre}: {self.comentario}"



# Clase Pregunta: Preguntas dentro de la sección Contacto
class Pregunta(models.Model):

  nombre = models.CharField(max_length=100)
  email = models.EmailField()
  telefono = models.IntegerField(blank=True)
  pregunta = models.TextField()

  def __str__(self):
    return f"{self.nombre}: {self.pregunta}"