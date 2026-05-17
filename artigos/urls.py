from django.urls import path
from . import views

app_name = 'artigos' 

urlpatterns = [
    path('', views.lista_artigos_view, name='lista_artigos'),
    path('<int:artigo_id>/', views.detalhe_artigo_view, name='detalhe_artigo'),
    path('novo/', views.novo_artigo_view, name='novo_artigo'),
    path('edita/<int:artigo_id>/', views.edita_artigo_view, name='edita_artigo'),
    path('like/<int:artigo_id>/', views.like_artigo_view, name='like_artigo'),
]