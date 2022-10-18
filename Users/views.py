from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from Users.forms import *
from datetime import datetime

# Create your views here.
def registerPage(request):
  
  formRegister = RegisterForm()

  if request.method == "POST":
    formRegister = RegisterForm(request.POST)
    print(formRegister)

    if formRegister.is_valid():
      formRegister.save()
      
      usuario = authenticate(username=formRegister.cleaned_data["username"],
                             password=formRegister.cleaned_data["password1"],
                             )
      
      login(request, usuario)
      return redirect("Blog:inicio")

  contexto = {"form": formRegister}

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



@login_required
def profile(request):

  usuario = request.user
  formAvatar = AvatarForm()
  formUser = UserEditForm(initial={"email": usuario.email, "first_name": usuario.first_name, 
                                   "last_name": usuario.last_name,})
  
  if request.method == "POST":

    if 'datos' in request.POST:
      formUser = UserEditForm(request.POST)
      
      if formUser.is_valid():
        
        info = formUser.cleaned_data
        print("info")
        usuario.email = info["email"]
        usuario.set_password(info["password1"])
        usuario.first_name = info["first_name"]
        usuario.last_name = info["last_name"]

        usuario.save()

        user = authenticate(username=usuario.username,
                              password=formUser.cleaned_data["password1"],
                              )
        
        login(request, user)

        return redirect("Blog:inicio")
      
    elif 'avatar' in request.POST:
      formAvatar = AvatarForm(request.POST, request.FILES)

      if formAvatar.is_valid():

        info = formAvatar.cleaned_data
        print(info)
        user = User.objects.get(username=request.user)

        avatar = Avatar(usuario=user, imagen=info["imagen"])

        if avatar == None:
          avatar.save()
        
        else:
          avatarViejo = Avatar.objects.get(usuario=user)
          avatarViejo.delete()
          
          avatar.save()

        return redirect("Blog:inicio")

  return render(request, "Users/profile.html", {"formUser": formUser, "formAvatar": formAvatar, "user": usuario, "hora": int(datetime.now().hour)})



@login_required
def avatarEliminar(request):

  user = User.objects.get(username=request.user)

  avatar = Avatar.objects.get(usuario=user)
  avatar.delete()

  return redirect("Blog:inicio")