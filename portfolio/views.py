from django.shortcuts import render, redirect, get_object_or_404
from .models import Licenciatura, Professor, Tecnologia, Projeto, UC, Competencia, TFC, Formacao
from .forms import ProjetoForm, TecnologiaForm, CompetenciaForm, FormacaoForm
from django.contrib.auth.decorators import login_required

# --- HOME & LISTAGENS ---

def home_page_view(request):
    return render(request, 'portfolio/home.html')

def licenciatura_view(request):
    return render(request, 'portfolio/licenciatura.html', {
        'licenciaturas': Licenciatura.objects.all()
    })

def professores_view(request):
    return render(request, 'portfolio/professores.html', {
        'professores': Professor.objects.all()
    })

def ucs_view(request):
    return render(request, 'portfolio/ucs.html', {
        'ucs': UC.objects.all()
    })

def tfcs_view(request):
    return render(request, 'portfolio/tfcs.html', {
        'tfcs': TFC.objects.all()
    })

def tecnologias_view(request):
    return render(request, 'portfolio/tecnologias.html', {
        'tecnologias': Tecnologia.objects.all()
    })

def projetos_view(request):
    return render(request, 'portfolio/projetos.html', {
        'projetos': Projeto.objects.all()
    })

def competencias_view(request):
    return render(request, 'portfolio/competencias.html', {
        'competencias': Competencia.objects.all()
    })

def formacao_view(request):
    return render(request, 'portfolio/formacao.html', {
        'formacoes': Formacao.objects.all()
    })


# --- CRUD PROJETO ---
@login_required
def novo_projeto_view(request):
    form = ProjetoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/novo_projeto.html', {'form': form})

@login_required
def edita_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/edita_projeto.html', {'form': form, 'projeto': projeto})

@login_required
def apaga_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    projeto.delete()
    return redirect('portfolio:projetos')


# --- CRUD TECNOLOGIA ---
@login_required
def nova_tecnologia_view(request):
    form = TecnologiaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/nova_tecnologia.html', {'form': form})

@login_required
def edita_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    form = TecnologiaForm(request.POST or None, request.FILES or None, instance=tecnologia)
    if form.is_valid():
        form.save()
        return redirect('portfolio:tecnologias')
    return render(request, 'portfolio/edita_tecnologia.html', {'form': form, 'tecnologia': tecnologia})

@login_required
def apaga_tecnologia_view(request, tecnologia_id):
    tecnologia = get_object_or_404(Tecnologia, id=tecnologia_id)
    tecnologia.delete()
    return redirect('portfolio:tecnologias')


# --- CRUD COMPETÊNCIA ---
@login_required
def nova_competencia_view(request):
    form = CompetenciaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/nova_competencia.html', {'form': form})

@login_required
def edita_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    form = CompetenciaForm(request.POST or None, instance=competencia)
    if form.is_valid():
        form.save()
        return redirect('portfolio:competencias')
    return render(request, 'portfolio/edita_competencia.html', {'form': form, 'competencia': competencia})

@login_required
def apaga_competencia_view(request, competencia_id):
    competencia = get_object_or_404(Competencia, id=competencia_id)
    competencia.delete()
    return redirect('portfolio:competencias')


# --- CRUD FORMAÇÃO ---
@login_required
def nova_formacao_view(request):
    form = FormacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacao')
    return render(request, 'portfolio/nova_formacao.html', {'form': form})

@login_required
def edita_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    form = FormacaoForm(request.POST or None, instance=formacao)
    if form.is_valid():
        form.save()
        return redirect('portfolio:formacao')
    return render(request, 'portfolio/edita_formacao.html', {'form': form, 'formacao': formacao})

@login_required
def apaga_formacao_view(request, formacao_id):
    formacao = get_object_or_404(Formacao, id=formacao_id)
    formacao.delete()
    return redirect('portfolio:formacao')