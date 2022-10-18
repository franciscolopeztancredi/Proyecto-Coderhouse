from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from datetime import datetime

from Blog.models import *
from Post.models import Post
from Blog.forms import *

# Create your views here.

hora = int(datetime.now().hour)



def inicio(request):

  usuarios = User.objects.all()
  posts = Post.objects.filter()

  contexto = {"hora": hora, "usuarios": usuarios, "usuariosTotal": usuarios.count(), "posts": posts}
  return render(request, "Blog/index.html", contexto)



def usuarioBuscar(request):

  usuarios = User.objects.all()
  posts = Post.objects.filter()

  contexto = {"hora": hora, "usuarios": usuarios, "usuariosTotal": usuarios.count(), "posts": posts}

  if request.GET["usuario"]:
    contexto["busqueda"] = request.GET["usuario"]
    contexto["usuario"] = User.objects.filter(username__icontains=request.GET["usuario"])

    return render(request, "Blog/index.html", contexto)



@login_required
def contacto(request):
  form = PreguntaForm()

  contexto = {"hora": hora, "form": form}

  if request.method == "POST":
    form = PreguntaForm(request.POST)

    print(form)
    if form.is_valid():
      form.save()

      return redirect("Blog:inicio")

  return render(request, "Blog/contacto.html", contexto)



@login_required
def about(request):

  return render(request, "Blog/about.html", {"hora": hora})