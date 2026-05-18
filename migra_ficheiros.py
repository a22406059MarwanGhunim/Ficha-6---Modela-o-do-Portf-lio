import os
import django
from django.core.files import File

# 1. Configurar o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

# Importar o BASE_DIR do settings para saber onde está a pasta media local
from django.conf import settings

# 2. Importar todos os modelos que contêm imagens
from artigos.models import Artigo
from escola.models import Curso
from portfolio.models import Projeto, Tecnologia, UC, TFC, MakingOFF

print("A iniciar a migração em massa de ficheiros para o Cloudinary...\n")

# --- 1. ARTIGOS (campo: fotografia) ---
print("-> A migrar Artigos...")
for obj in Artigo.objects.all():
    if obj.fotografia and obj.fotografia.name:
        # CORREÇÃO: Construir o caminho local manualmente em vez de usar .path
        local_path = os.path.join(settings.BASE_DIR, 'media', obj.fotografia.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.fotografia.save(os.path.basename(local_path), File(f), save=True)
            print(f"   [OK] Artigo migrado: {obj}")

# --- 2. CURSOS (campo: imagem) ---
print("\n-> A migrar Cursos...")
for obj in Curso.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(settings.BASE_DIR, 'media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"   [OK] Curso migrado: {obj}")

# --- 3. PROJETOS (campo: imagem) ---
print("\n-> A migrar Projetos...")
for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(settings.BASE_DIR, 'media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"   [OK] Projeto migrado: {obj}")

# --- 4. TECNOLOGIAS (campo: logo) ---
print("\n-> A migrar Tecnologias...")
for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:
        local_path = os.path.join(settings.BASE_DIR, 'media', obj.logo.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.logo.save(os.path.basename(local_path), File(f), save=True)
            print(f"   [OK] Tecnologia migrada: {obj}")

# --- 5. UCs (campo: imagem) ---
print("\n-> A migrar UCs...")
for obj in UC.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(settings.BASE_DIR, 'media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"   [OK] UC migrada: {obj}")

# --- 6. TFC (campo: imagem) ---
print("\n-> A migrar TFCs...")
for obj in TFC.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join(settings.BASE_DIR, 'media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"   [OK] TFC migrado: {obj}")

# --- 7. MAKING OFF (campo: FotoCaderno) ---
print("\n-> A migrar Making OFF...")
for obj in MakingOFF.objects.all():
    if obj.FotoCaderno and obj.FotoCaderno.name:
        local_path = os.path.join(settings.BASE_DIR, 'media', obj.FotoCaderno.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.FotoCaderno.save(os.path.basename(local_path), File(f), save=True)
            print(f"   [OK] MakingOFF migrado: {obj}")

print("\n[PROCESSO CONCLUÍDO] Todos os ficheiros locais foram enviados para a Cloud!")