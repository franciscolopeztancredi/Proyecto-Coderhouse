from django.urls import path

# Importo las views
from Blog import views

app_name = 'Blog'
urlpatterns = [
  path('', views.inicio, name="inicio"),
  path('post/<int:num>', views.entrada, name="post"),
  path('publicar/', views.entradaNuevo, name="publicar"),
  path('buscar/entrada/', views.entradaBuscar, name="buscarEntrada"),
  path('buscar/usuario/', views.usuarioBuscar, name="buscarUsuario"),
  path('contacto', views.contacto, name="contacto"),
]