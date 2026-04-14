
import json
import os
from django.core.management.base import BaseCommand

from portfolio.models import UC


class Command(BaseCommand):
    help = "Carrega todas as UCs dos JSONs da Lusófona para a base de dados"

    def handle(self, *args, **options):
        pasta_jsons = "data/lusofona"
        
        if not os.path.exists(pasta_jsons):
            self.stdout.write(self.style.ERROR(f"Pasta não encontrada: {pasta_jsons}"))
            return

        ficheiros = [f for f in os.listdir(pasta_jsons) if f.endswith("-PT.json")]
        
        self.stdout.write(f"Encontrados {len(ficheiros)} ficheiros de UC (versão PT). A importar...")

        criados = 0
        atualizados = 0
        ignorados = 0

        for ficheiro in ficheiros:
            caminho = os.path.join(pasta_jsons, ficheiro)
            
            try:
                with open(caminho, "r", encoding="utf-8") as f:
                    dados = json.load(f)

                # Extrair dados importantes
                codigo_legivel = dados.get("curricularIUnitReadableCode")
                nome = dados.get("curricularUnitName")
                
                if not codigo_legivel or not nome:
                    ignorados += 1
                    continue

                # Criar ou atualizar a UC
                uc, criado = UC.objects.update_or_create(
                    codigo_legivel=codigo_legivel,
                    defaults={
                        "course_code": dados.get("courseCode", 0),
                        "nome": nome,
                        "semestre": "",                          # não existe na API
                        "ano": dados.get("curricularYear"),
                        "creditos": dados.get("ects", 0),
                        "descricao": dados.get("objectives", ""),
                        "programa": dados.get("programme", ""),
                        "avaliacao": dados.get("avaliacao", ""),
                        "obrigatorio": dados.get("nature") == "Obrigatório",
                        "lingua": dados.get("languageCode", "PT"),
                        "URL": "",                               # podes preencher depois se quiseres
                    }
                )

                if criado:
                    criados += 1
                    self.stdout.write(f"✅ Criado: {codigo_legivel} - {nome}")
                else:
                    atualizados += 1
                    self.stdout.write(f"🔄 Atualizado: {codigo_legivel} - {nome}")

            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Erro no ficheiro {ficheiro}: {e}"))
                ignorados += 1

        self.stdout.write(self.style.SUCCESS(
            f"\nImportação concluída!\n"
            f"Criados: {criados} | Atualizados: {atualizados} | Ignorados: {ignorados}"
        ))