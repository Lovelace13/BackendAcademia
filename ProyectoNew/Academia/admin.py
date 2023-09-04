from django.contrib import admin

# Register your models here.
from .models import Materia,Aula,Profesor

admin.site.register(Materia)
admin.site.register(Aula)
admin.site.register(Profesor)