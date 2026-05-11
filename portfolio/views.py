from django.shortcuts import render

from .models import Licenciatura, Professor, Tecnologia, Projeto, UC, Competencia, TFC, Formacao

def licenciatura_view(request):
    return render(request, 'portfolio/licenciatura.html', {
        'licenciaturas': Licenciatura.objects.all()
    })

def professores_view(request):
    return render(request, 'portfolio/professores.html', {
        'professores': Professor.objects.all()
    })

def tecnologias_view(request):
    return render(request, 'portfolio/tecnologias.html', {
        'tecnologias': Tecnologia.objects.all()
    })

def projetos_view(request):
    return render(request, 'portfolio/projetos.html', {
        'projetos': Projeto.objects.all()
    })

def ucs_view(request):
    return render(request, 'portfolio/ucs.html', {
        'ucs': UC.objects.all()
    })

def competencias_view(request):
    return render(request, 'portfolio/competencias.html', {
        'competencias': Competencia.objects.all()
    })

def tfcs_view(request):
    return render(request, 'portfolio/tfcs.html', {
        'tfcs': TFC.objects.all()
    })

def formacao_view(request):
    return render(request, 'portfolio/formacao.html', {
        'formacoes': Formacao.objects.all()
    })

def home_page_view(request):
    return render(request, 'portfolio/home.html')