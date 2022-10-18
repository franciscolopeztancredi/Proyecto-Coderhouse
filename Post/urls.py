from django.urls import path

# Importo las views
from Post import views

app_name = 'Post'
urlpatterns = [
  path('<int:num>/', views.entrada, name="entrada"),
  path('<int:num>/editar', views.entradaEditar, name="entradaEditar"),
  path('<int:num>/eliminar', views.entradaEliminar, name="entradaEliminar"),
  path('publicar/', views.entradaNuevo, name="entradaNuevo"),
  path('buscar/entrada/', views.entradaBuscar, name="entradaBuscar"),  
]