from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    # --- HOME & LISTAGENS ---
    path('', views.home_page_view, name='home'),
    path('licenciatura/', views.licenciatura_view, name='licenciatura'),
    path('professores/', views.professores_view, name='professores'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('ucs/', views.ucs_view, name='ucs'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('formacao/', views.formacao_view, name='formacao'),

    # --- CRUD PROJETO ---
    path('projeto/novo/', views.novo_projeto_view, name='novo_projeto'),
    path('projeto/edita/<int:projeto_id>/', views.edita_projeto_view, name='edita_projeto'),
    path('projeto/apaga/<int:projeto_id>/', views.apaga_projeto_view, name='apaga_projeto'),

    # --- CRUD TECNOLOGIA ---
    path('tecnologia/nova/', views.nova_tecnologia_view, name='nova_tecnologia'),
    path('tecnologia/edita/<int:tecnologia_id>/', views.edita_tecnologia_view, name='edita_tecnologia'),
    path('tecnologia/apaga/<int:tecnologia_id>/', views.apaga_tecnologia_view, name='apaga_tecnologia'),

    # --- CRUD COMPETÊNCIA ---
    path('competencia/nova/', views.nova_competencia_view, name='nova_competencia'),
    path('competencia/edita/<int:competencia_id>/', views.edita_competencia_view, name='edita_competencia'),
    path('competencia/apaga/<int:competencia_id>/', views.apaga_competencia_view, name='apaga_competencia'),

    # --- CRUD FORMAÇÃO ---
    path('formacao/nova/', views.nova_formacao_view, name='nova_formacao'),
    path('formacao/edita/<int:formacao_id>/', views.edita_formacao_view, name='edita_formacao'),
    path('formacao/apaga/<int:formacao_id>/', views.apaga_formacao_view, name='apaga_formacao'),
]