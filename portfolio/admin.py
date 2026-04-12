from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Licenciatura)
class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'semestre', 'creditos')
    search_fields = ('nome',)
    list_filter = ('duracao',)


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    filter_horizontal = ('Disciplina',)

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'interesseNivel')
    search_fields = ('nome', 'tipo')
    list_filter = ('tipo',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'dataRealizacao')
    search_fields = ('titulo',)
    list_filter = ('dataRealizacao',)

@admin.register(UC)
class UCAdmin(admin.ModelAdmin):
    list_display = ('nome', 'creditos')
    search_fields = ('nome',)

@admin.register(TFC)
class TFCAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'orientador', 'destaque')
    search_fields = ('titulo',)
    list_filter = ('destaque',)

@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'nivel',)
    search_fields = ('nome', 'tipo')
    list_filter = ('nivel',)

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'instituicao', 'dataInicio', 'dataConclusao', 'tipo')
    search_fields = ('titulo', 'instituicao')
    list_filter = ('tipo',)

@admin.register(MakingOFF)
class MakingOFFAdmin(admin.ModelAdmin):
    list_display = ('usoAI',)
    list_filter = ('usoAI',)