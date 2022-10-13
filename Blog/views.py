from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

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

  form = ComentarioForm()
  contexto = {"hora": hora, "form": form}

  if 0 < num <= Post.objects.count():
    post = Post.objects.get(id=num)
    contexto["post"] = post

  if request.method == 'POST':

    form = ComentarioForm(request.POST)

    if form.is_valid:

          informacion = form.cleaned_data

          comment = Comentario(nombre=request.user, comentario=informacion['comentario'], post=Post.objects.get(id=num))
          comment.save()

          return render(request, "Blog/post.html", contexto)

  return render(request, "Blog/post.html", contexto)



def entradaNuevo(request):

  if request.user.is_superuser:
    num = Post.objects.count() + 1
    form = PostForm()

    contexto = {"hora": hora, "form": form, "num": num}

    if request.method == "POST":
      form = PostForm(request.POST)

      print(form)
      if form.is_valid():
        form.save()

        return redirect("Blog:inicio")
  else:

    return redirect("Blog:inicio")

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