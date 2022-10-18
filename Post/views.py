from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

from Post.models import *
from Post.forms import *
from datetime import datetime
# Create your views here.
def entrada(request, num):

  form = ComentarioForm()
  contexto = {"hora": int(datetime.now().hour), "form": form}

  if 0 < num <= Post.objects.count():
    post = Post.objects.get(num_entrada=num)
    contexto["post"] = post

  if request.method == 'POST':

    form = ComentarioForm(request.POST)
    print(form)

    if form.is_valid:

      info = form.cleaned_data

      comment = Comentario(nombre=request.user, comentario=info['comentario'], post=Post.objects.get(num_entrada=num))
      comment.save()

      return render(request, "Post/post.html", contexto)

  return render(request, "Post/post.html", contexto)



def entradaNuevo(request):

  if request.user.is_superuser:

    num = Post.objects.count() + 1
    form = PostForm()

    contexto = {"hora": int(datetime.now().hour), "form": form, "num": num}

    if request.method == "POST":
      form = PostForm(request.POST)

      print(form)
      if form.is_valid():
        form.save()

        return redirect("Blog:inicio")

  else:

    return redirect("Blog:inicio")

  return render(request, "Post/postCrear.html", contexto)



def entradaBuscar(request):

  usuarios = User.objects.all()
  posts = Post.objects.filter()

  contexto = {"hora": int(datetime.now().hour), "usuarios": usuarios, "usuariosTotal": usuarios.count(), "posts": posts}

  if request.GET["titulo"]:
    
    contexto["titulo"] = request.GET["titulo"]
    contexto["post"] = Post.objects.filter(titulo__icontains=request.GET["titulo"])

    return render(request, "Blog/index.html", contexto)



@staff_member_required
def entradaEditar(request, num):

  post = Post.objects.get(num_entrada=num)
  num_total = Post.objects.count() + 1
  form = PostForm()

  if request.method == "POST":

    form = PostForm(request.POST)

    if form.is_valid():
      
      info = form.cleaned_data

      post.titulo = info["titulo"]
      post.fecha = info["fecha"]
      post.autor = info["autor"]
      post.image = info["image"]
      post.texto = info["texto"]

      post.save()
      return redirect("Blog:inicio")
    
  else:

    form = PostForm(initial={"titulo": post.titulo, "fecha": post.fecha, "autor": post.autor,
    "image": post.image, "texto": post.texto})
  
  contexto = {"hora": int(datetime.now().hour), "form": form, "num": num_total, "post": post}
  return render(request, "Post/postEditar.html", contexto)



@staff_member_required
def entradaEliminar(request, num):

  post = Post.objects.get(num_entrada=num)
  post.delete()

  return redirect("Blog:inicio")