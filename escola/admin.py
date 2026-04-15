from django.contrib import admin
from .models import *


@admin.site.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

@admin.site.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero')

@admin.site.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'professor')