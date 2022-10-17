from django.urls import path

# Importo las views
from Blog import views

app_name = 'Blog'
urlpatterns = [
  path('', views.inicio, name="inicio"),
  path('post/<int:num>', views.entrada, name="entrada"),
  path('publicar/', views.entradaNuevo, name="entradaNuevo"),
  path('post/<int:num>/editar', views.entradaEditar, name="entradaEditar"),
  path('post/<int:num>/eliminar', views.entradaEliminar, name="entradaEliminar"),
  path('buscar/entrada/', views.entradaBuscar, name="entradaBuscar"),
  path('buscar/usuario/', views.usuarioBuscar, name="buscarUsuario"),
  path('contacto', views.contacto, name="contacto"),
  path('about/', views.about, name="about")
]