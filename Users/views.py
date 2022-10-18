from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from Users.forms import *

# Create your views here.
def registerPage(request):
  
  form = RegisterForm()

  if request.method == "POST":
    form = RegisterForm(request.POST)
    print(form)

    if form.is_valid():
      form.save()
      user = form.cleaned_data.get("username")
      # messages.success(request, f"El usuario {user} ha sido registrado de forma exitosa.")
      usuario = authenticate(username=form.cleaned_data["username"],
                             password=form.cleaned_data["password1"],
                             )
      
      login(request, usuario)
      return redirect("Blog:inicio")

  contexto = {"form": form}

  return render(request, "Users/register.html", contexto)



def loginPage(request):

  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect("Blog:inicio")
    else:
      messages.info(request, "Usuario o contraseña incorrecta")

  contexto = {}
  return render(request, "Users/login.html", contexto)



def logoutUser(request):
  
  logout(request)

  return redirect("Users:login")



def profile(request):

  user = request.user
  
  if request.method == "POST":
    form = UserEditForm()

  contexto = {"user": user}
  return render(request, "Users/profile.html", contexto)