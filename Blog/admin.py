from django.contrib import admin

# Importo mis modelos
from Blog.models import *

# Registro mis modelos
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Pregunta)