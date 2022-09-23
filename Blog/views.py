from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from datetime import datetime

from Blog.models import *
from Blog.forms import *

# Create your views here.

hora = int(datetime.now().hour)

def inicio(request):

  usuarios = User.objects.all()
  posts = Post.objects.filter()
  tags = Tag.objects.all()

  contexto = {"hora": hora, "usuarios": usuarios, "usuariosTotal": usuarios.count(), "posts": posts, "tags": tags}
  return render(request, "Blog/index.html", contexto)



def entrada(request, num):

  post = Post.objects.filter()
  postNum = Post.objects.count()

  url = int(request.path[-1])

  form = ComentarioForm()
  contexto = {"hora": hora, "num": num, "posts": post, "url": url, "postNum": postNum, "form": form}

  if request.method == 'POST':

    form = ComentarioForm(request.POST)

    print(form)

    if form.is_valid:

          informacion = form.cleaned_data

          comment = Comentario(nombre=request.user, comentario=informacion['comentario'], post=Post.objects.get(id=num))

          comment.save()

          return render(request, "Blog/post.html", contexto)

  return render(request, "Blog/post.html", contexto)



def entradaNuevo(request):
  num = Post.objects.count() + 1
  form = PostForm()

  contexto = {"hora": hora, "form": form, "num": num}

  if request.method == "POST":
    form = PostForm(request.POST)

    print(form)
    if form.is_valid():
      form.save()

      return redirect("inicio")

  return render(request, "Blog/publicar.html", contexto)



def entradaBuscar(request):

  usuarios = User.objects.all()
  posts = Post.objects.filter()
  tags = Tag.objects.all()

  contexto = {"hora": hora, "usuarios": usuarios, "usuariosTotal": usuarios.count(), "posts": posts, "tags": tags}

  if request.GET["titulo"]:
    
    contexto["titulo"] = request.GET["titulo"]
    contexto["post"] = Post.objects.filter(titulo__icontains=request.GET["titulo"])

    return render(request, "Blog/index.html", contexto)



def usuarioBuscar(request):

  usuarios = User.objects.all()
  posts = Post.objects.filter()
  tags = Tag.objects.all()

  contexto = {"hora": hora, "usuarios": usuarios, "usuariosTotal": usuarios.count(), "posts": posts, "tags": tags}

  if request.GET["usuario"]:
    contexto["busqueda"] = request.GET["usuario"]
    contexto["usuario"] = User.objects.filter(username__icontains=request.GET["usuario"])

    return render(request, "Blog/index.html", contexto)



def registerPage(request):
  
  form = RegisterForm()

  if request.method == "POST":
    form = RegisterForm(request.POST)

    if form.is_valid():
      form.save()
      user = form.cleaned_data.get("username")
      messages.success(request, f"El usuario {user} ha sido registrado de forma exitosa.")

      return redirect("login")

  contexto = {"form": form}

  return render(request, "Blog/register.html", contexto)



def loginPage(request):

  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect("inicio")
    else:
      messages.info(request, "Usuario o contraseña incorrecta")

  contexto = {}
  return render(request, "Blog/login.html", contexto)



def logoutUser(request):
  
  logout(request)

  return redirect("login")



def contacto(request):
  form = PreguntaForm()

  contexto = {"hora": hora, "form": form}

  if request.method == "POST":
    form = PreguntaForm(request.POST)

    print(form)
    if form.is_valid():
      form.save()

      return redirect("inicio")

  return render(request, "Blog/contacto.html", contexto)