from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'), # Página principal do portfólio
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('professores/', views.professores_view, name='professores'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('formacao/', views.formacao_view, name='formacao'),
]