from django.urls import path, include
from Users import views

app_name = 'Users'
urlpatterns = [
  path('signup/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutUser, name="logout"),
  path('profile/', views.profile, name="profile"),
  path('profile/avatar/eliminar', views.avatarEliminar, name="avatarEliminar"),
  path('messages/', views.mensajes, name="mensajes"),
  path('messages/eliminar/<int:num>', views.mensajesEliminar, name="mensajesEliminar"),
]