# portfolio/management/commands/carregar_tfc.py

import json
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import urllib.request
import os

from portfolio.models import TFC, Professor, Licenciatura, Tecnologia, Competencia


class Command(BaseCommand):
    help = "Carrega os TFCs do ficheiro JSON para a base de dados"

    def handle(self, *args, **options):
        caminho_json = "data/TFCS.json"

        self.stdout.write("A ler o ficheiro TFCS.json...")

        with open(caminho_json, "r", encoding="utf-8") as f:
            dados = json.load(f)

        # Se o JSON for um único objeto em vez de lista
        if isinstance(dados, dict):
            dados = [dados]

        criados = 0
        atualizados = 0

        for item in dados:
            try:
                # 1. Orientador (Professor)
                orientador, _ = Professor.objects.get_or_create(
                    nome=item.get("orientador", "Desconhecido"),
                    defaults={
                        "email": "orientador@ulusofona.pt",
                        "URL": "https://teses.deisi.ulusofona.pt/"
                    }
                )

                # 2. Licenciatura
                lic_str = item.get("licenciaturas", "")
                nome_lic = lic_str.split(".")[0].strip() if "." in lic_str else lic_str

                licenciatura, _ = Licenciatura.objects.get_or_create(
                    nome=nome_lic,
                    defaults={
                        "Instituicao": "Universidade Lusófona",
                        "duracao": 3,
                        "creditos": 180,
                        "semestre": "2025"
                    }
                )

                # 3. Tecnologias
                tecnologias = []
                for tech_nome in item.get("tecnologias usadas", []):
                    tech, _ = Tecnologia.objects.get_or_create(
                        nome=tech_nome,
                        defaults={
                            "tipo": "Linguagem/Ferramenta",
                            "descricao": f"Tecnologia: {tech_nome}",
                            "URL": "#",
                            "interesseNivel": 7
                        }
                    )
                    tecnologias.append(tech)

                # 4. Áreas (Competencias)
                areas = []
                for area_nome in item.get("áreas", []):
                    area, _ = Competencia.objects.get_or_create(
                        nome=area_nome,
                        defaults={
                            "tipo": "Área Temática",
                            "nivel": 8,
                            "descricao": f"Área: {area_nome}"
                        }
                    )
                    areas.append(area)

                # 5. Criar ou atualizar o TFC
                tfc, criado = TFC.objects.update_or_create(
                    titulo=item["titulo"],
                    autor=item.get("nome", ""),
                    defaults={
                        "orientador": orientador,
                        "licenciatura": licenciatura,
                        "descricao": item.get("resumo", "")[:200],
                        "URL": item.get("link para PDF", ""),
                        "destaque": False,
                    }
                )

                # ManyToMany
                tfc.tecnologia.set(tecnologias)
                tfc.area.set(areas)

                # 6. Imagem (tenta guardar se existir)
                url_imagem = item.get("imagem")
                if url_imagem and not tfc.imagem:
                    try:
                        with urllib.request.urlopen(url_imagem) as resposta:
                            nome_ficheiro = os.path.basename(url_imagem) or "imagem.jpg"
                            tfc.imagem.save(nome_ficheiro, ContentFile(resposta.read()), save=True)
                        self.stdout.write(f"   ✓ Imagem guardada: {item['titulo']}")
                    except:
                        pass   # ignora se não conseguir baixar a imagem

                if criado:
                    criados += 1
                    self.stdout.write(f"✅ Criado: {item['titulo']}")
                else:
                    atualizados += 1
                    self.stdout.write(f"🔄 Atualizado: {item['titulo']}")

            except Exception as e:
                self.stdout.write(f"❌ Erro ao processar '{item.get('titulo', 'sem título')}': {e}")

        self.stdout.write(self.style.SUCCESS(
            f"\n✅ Concluído! Criados: {criados} | Atualizados: {atualizados}"
        ))