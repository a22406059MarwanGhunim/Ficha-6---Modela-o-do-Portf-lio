from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Artigo, Comentario
from .forms import ArtigoForm, ComentarioForm

# Função auxiliar para verificar se pertence ao grupo autores
def e_autor(user):
    return user.groups.filter(name='autores').exists()

# 1. Listagem completa (Qualquer pessoa vê)
def lista_artigos_view(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/lista.html', {'artigos': artigos})

# 2. Detalhe do Artigo (Vê artigos, comentários e adiciona comentário se logado)
def detalhe_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    comentarios = artigo.comentarios.all().order_by('-data_criacao')
    
    form = None
    if request.user.is_authenticated:
        form = ComentarioForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            comentario = form.save(commit=False)
            comentario.artigo = artigo
            comentario.autor = request.user
            comentario.save()
            return redirect('artigos:detalhe_artigo', artigo_id=artigo.id)

    return render(request, 'artigos/detalhe.html', {
        'artigo': artigo,
        'comentarios': comentarios,
        'form': form
    })

# 3. Criar Artigo (Apenas grupo autores)
@login_required
@user_passes_test(e_autor)
def novo_artigo_view(request):
    form = ArtigoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        artigo = form.save(commit=False)
        artigo.autor = request.user # Associa o artigo ao utilizador logado
        artigo.save()
        return redirect('artigos:lista_artigos')
    return render(request, 'artigos/novo.html', {'form': form})

# 4. Editar Artigo (Apenas o próprio autor)
@login_required
@user_passes_test(e_autor)
def edita_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    
    # Segurança: Bloqueia se o utilizador logado não for o dono do artigo
    if artigo.autor != request.user:
        return render(request, 'artigos/erro_permissao.html')
        
    form = ArtigoForm(request.POST or None, request.FILES or None, instance=artigo)
    if form.is_valid():
        form.save()
        return redirect('artigos:detalhe_artigo', artigo_id=artigo.id)
    return render(request, 'artigos/edita.html', {'form': form, 'artigo': artigo})

# 5. Funcionalidade de Likes (Qualquer pessoa autenticada pode dar like)
@login_required
def like_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if artigo.likes.filter(id=request.user.id).exists():
        artigo.likes.remove(request.user) # Retira o like se já clicou antes
    else:
        artigo.likes.add(request.user) # Adiciona o like
    return redirect(request.META.get('HTTP_REFERER', 'artigos:lista_artigos'))