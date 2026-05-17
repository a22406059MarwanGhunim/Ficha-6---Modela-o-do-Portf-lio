# Making Off - Ficha 8: Implementação de Operações CRUD no Portfólio

Este documento detalha o processo de desenvolvimento, as decisões técnicas, as dificuldades encontradas e as respetivas resoluções durante a implementação das operações completas de CRUD (Create, Read, Update, Delete) no meu projeto Django.

## 1. O Que Foi Feito (DescricaoDecisoes)
* **Criação de Formulários Automatizados:** Implementei o ficheiro `portfolio/forms.py` utilizando `ModelForm` para os modelos `Projeto`, `Tecnologia`, `Competencia` e `Formacao`. Isto permitiu gerar formulários HTML automáticos e seguros com base nos campos definidos no `models.py`.
* **Desenvolvimento de Views Dinâmicas:** Adicionei três novas funções de controlo (views) no `portfolio/views.py` para cada um dos quatro modelos:
  * Uma view para criação (ex: `novo_projeto_view`).
  * Uma view para edição (ex: `edita_projeto_view`) recorrendo ao `get_object_or_404` para capturar o registo pelo ID.
  * Uma view para eliminação (ex: `apaga_projeto_view`) com redirecionamento automático após a exclusão.
* **Mapeamento de Rotas (URLs):** Atualizei o `portfolio/urls.py` com rotas dinâmicas que aceitam argumentos inteiros (ex: `<int:projeto_id>/`) para identificar os registos nas operações de edição e remoção.
* **Interface de Utilizador (Templates):** 
  * Criei 8 novos ficheiros HTML (2 para cada modelo: um de criação e um de edição) contendo a tag `{{ form.as_p }}` e proteção `{% csrf_token %}`.
  * Atualizei os 4 ficheiros de listagem originais (`projetos.html`, `tecnologias.html`, `competencias.html`, `formacao.html`) para incluir botões de ação estruturados para criar, editar e apagar elementos.

## 2. Dificuldades Sentidas (Erros)
* **Falha no Upload de Imagens:** Inicialmente, ao tentar criar ou editar Projetos e Tecnologias, as imagens/logos associados não eram guardados na base de dados, embora os campos de texto funcionassem bem.
* **Erros de Redirecionamento (NoReverseMatch):** Encontrei erros ao tentar usar a tag `{% url %}` nos botões de Editar e Apagar, pois o Django não conseguia mapear os links corretamente.
* **Estilo Visual Confuso:** O excesso de estilos inline e CSS complexo gerado inicialmente estava a tornar o código dos templates difícil de ler, depurar e manter.

## 3. Como Foram Resolvidas (Correcoes)
* **Correção do Enctype nos Formulários:** Resolvi o problema das imagens adicionando o atributo `enctype="multipart/form-data"` à tag `<form>` nos templates de Projeto e Tecnologia. Garanti também que as views recebiam `request.FILES`.
* **Ajuste de Argumentos nas URLs:** Corrigi os erros de `NoReverseMatch` garantindo que o nome da variável no `urls.py` (`<int:projeto_id>/`) era exatamente o mesmo usado como argumento na view (`projeto_id`) e na tag do template (`projeto.id`).
* **Simplificação dos Templates (Clean Code):** Fiz um "fuse" limpo entre a lógica CRUD e o meu design original. Removi os estilos desnecessários, mantendo apenas a estrutura semântica do HTML (`<section>`, `<article>`) e as molduras básicas de organização.

## 4. Justificação Técnico-Pedagógica (Justificacao)
* A escolha de usar `ModelForm` justificou-se pela rapidez de desenvolvimento e validação automática de dados nativa do Django, evitando código repetitivo.
* A separação das operações por ID garante a integridade dos dados e uma experiência de utilização limpa, onde consigo gerir o meu percurso académico e competências de forma totalmente autónoma diretamente pelo browser.

## 5. Uso de Inteligência Artificial (usoAI)
* **Sim.** Utilizei o assistente de IA para alguns processos de debug