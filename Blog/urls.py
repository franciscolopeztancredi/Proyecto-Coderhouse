from django.urls import path

# Importo las views
from Blog import views

app_name = 'Blog'
urlpatterns = [
  path('', views.inicio, name="inicio"),
  path('buscar/usuario/', views.usuarioBuscar, name="buscarUsuario"),
  path('contacto', views.contacto, name="contacto"),
  path('about/', views.about, name="about")
]