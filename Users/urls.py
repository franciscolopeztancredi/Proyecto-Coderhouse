from django.urls import path, include
from Users import views

app_name = 'Users'
urlpatterns = [
  path('signup/', views.registerPage, name="register"),
  path('login/', views.loginPage, name="login"),
  path('logout/', views.logoutUser, name="logout"),
]