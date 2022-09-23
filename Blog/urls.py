from django.urls import path

# Importo las views
from Blog import views

urlpatterns = [
  path('', views.inicio, name="inicio"),
  path('post/<num>', views.entrada, name="post"),
  path('publicar/', views.entradaNuevo, name="publicar"),
  path('buscar/entrada/', views.entradaBuscar, name="buscarEntrada"),
  path('register/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutUser, name="logout"),
  path('buscar/usuario/', views.usuarioBuscar, name="buscarUsuario"),
  path('contacto', views.contacto, name="contacto"),
]