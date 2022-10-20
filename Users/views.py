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
        usuario.email = info["email"]
        usuario.set_password(info["password1"])
        usuario.first_name = info["first_name"]
        usuario.last_name = info["last_name"]

        usuario.save()

        user = authenticate(username=usuario.username,
                              password=formUser.cleaned_data["password1"],
                              )
        
        login(request, user)

        return redirect("Users:profile")
      
    elif 'avatar' in request.POST:
      formAvatar = AvatarForm(request.POST, request.FILES)

      if formAvatar.is_valid():

        info = formAvatar.cleaned_data
        user = User.objects.get(username=request.user)

        avatar = Avatar(usuario=user, imagen=info["imagen"])

        try:
          avatarViejo = Avatar.objects.get(usuario=user)
          avatarViejo.delete()
          
          avatar.save()
          
        except:
          avatar.save()

        return redirect("Users:profile")

  return render(request, "Users/profile.html", {"formUser": formUser, "formAvatar": formAvatar, "user": usuario, "hora": int(datetime.now().hour)})



@login_required
def avatarEliminar(request):

  avatar = Avatar.objects.get(usuario=request.user)
  avatar.delete()

  return redirect("Users:profile")



@login_required
def mensajes(request):

  mensajes = Mensajes.objects.all()
  formMensaje = MensajesForm()

  if request.method == 'POST':

    formMensaje = MensajesForm(request.POST)
    print(formMensaje)

    if formMensaje.is_valid:

      info = formMensaje.cleaned_data

      mensaje = Mensajes(usuario = request.user, mensaje=info['mensaje'], numero=(mensajes.count()+1))
      mensaje.save()

      return render(request, "Users/messages.html", {"mensajes": mensajes, "form": formMensaje, "hora": int(datetime.now().hour)})
  return render(request, "Users/messages.html", {"mensajes": mensajes, "form": formMensaje, "hora": int(datetime.now().hour)})



@login_required
def mensajesEliminar(request, num):
  mensaje = Mensajes.objects.get(numero=num)
  mensaje.delete()

  return redirect("Users:mensajes")