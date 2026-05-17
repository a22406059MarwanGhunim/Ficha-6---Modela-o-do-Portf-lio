from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.contrib.auth.models import Group 

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('portfolio:home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('portfolio:home')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Vai buscar ou cria o grupo 'autores' e adiciona o utilizador
            grupo_autores, created = Group.objects.get_or_create(name='autores')
            user.groups.add(grupo_autores)
            
            login(request, user) # Faz login automático após registo, se desejares
            return redirect('portfolio:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def magic_link_request_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            # Procura o utilizador pelo email fornecido
            user = User.objects.get(email=email)
            
            # Gera o token e o ID codificado do utilizador
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Constrói o link absoluto
            # Nota: se mudares de porta (ex: 8000), o request.get_host() apanha automaticamente
            link = f"http://{request.get_host()}/accounts/magic-login/{uid}/{token}/"
            
            # Envia o "email" (vai aparecer no teu terminal onde corre o runserver)
            send_mail(
                'O teu Link Mágico de Acesso',
                f'Clica no seguinte link para entrar no portfólio:\n\n{link}',
                'noreply@portfolio.com',
                [user.email],
                fail_silently=False,
            )
            messages.success(request, "Link mágico enviado! Verifica o teu terminal/consola.")
        except User.objects.model.DoesNotExist:
            # Por segurança, podes dar a mesma mensagem para não revelar emails registados
            messages.success(request, "Se o email existir no sistema, um link foi enviado.")
            
    return render(request, 'accounts/magic_link_request.html')


def magic_login_view(request, uidb64, token):
    try:
        # Descodifica o ID do utilizador
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.objects.model.DoesNotExist):
        user = None

    # Verifica se o utilizador existe e se o token ainda é válido
    if user is not None and default_token_generator.check_token(user, token):
        login(request, user)
        messages.success(request, f"Bem-vindo de volta, {user.username}!")
        return redirect('portfolio:home')
    else:
        messages.error(request, "O link mágico é inválido ou já expirou.")
        return redirect('accounts:login')