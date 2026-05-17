# Making Off - Ficha 9: Autenticação Avançada e Permissões no Portfólio

Este documento descreve detalhadamente o processo de planeamento, implementação e resolução de problemas relativos à segurança, sistemas de autenticação (Senha e Link Mágico) e gestão de acessos por grupos no projeto.

## 1. O Que Foi Feito (DescricaoDecisoes)
* **Criação da App de Autenticação (`accounts`):** Desenvolvi uma nova aplicação isolada para gerir o ciclo de vida dos utilizadores, garantindo a modularidade do projeto Django.
* **Formulários Customizados de Registo:** Criei o `CustomUserCreationForm` herdando de `UserCreationForm` para incluir a obrigatoriedade do campo de email no registo de novas contas.
* **Fluxo de Autenticação Tradicional:** Implementei views robustas recorrendo às funções nativas do Django (`authenticate`, `login`, `logout`) para validar utilizadores e gerir sessões de forma segura.
* **Implementação de Link Mágico (Magic Link):** Desenvolvi um sistema de login alternativo sem palavra-passe. O utilizador insere o email, o sistema gera um token seguro e único (`default_token_generator`) e codifica o ID do utilizador em Base64 (`urlsafe_base64_encode`).
* **Configuração de Email em Desenvolvimento:** Configurei o `EMAIL_BACKEND` no `settings.py` para redirecionar os emails gerados para o terminal do servidor, permitindo copiar e testar os links mágicos localmente de forma eficaz.
* **Criação da App `artigos`:** Desenvolvi uma aplicação completa de blog/conteúdos, contendo o modelo `Artigo` (com chave estrangeira para o `User`), sistema de comentários associado e um campo `ManyToManyField` para registar gostos (Likes).
* **Automação de Grupos no Registo:** Modifiquei a view de registo para que qualquer novo utilizador criado através do site seja inserido automaticamente no grupo `autores` da base de dados.
* **Segurança ao Nível do Objeto e Decoradores:** 
  * Apliquei o decorador `@login_required` e a validação `@user_passes_test` nas views críticas para trancar os formulários CRUD.
  * Implementei lógica na view de edição de artigos para garantir que um utilizador autenticado apenas consiga modificar um artigo se for o autor original (`artigo.autor == request.user`).

## 2. Dificuldades Sentidas (Erros)
* **Erro de Namespace Inexistente (`NoReverseMatch`):** Ao integrar o link do blog no menu principal, o Django crashou com a mensagem de que `'artigos' is not a registered namespace`, impedindo a renderização da página inicial.
* **Crash no Modelo por Argumento Inválido (`TypeError`):** O servidor recusou-se a arrancar devido a um erro de compilação no `artigos/models.py`, gerado por um argumento incorreto no campo de imagem (`upload_url`).
* **Falha de Permissões ao Forçar URLs:** Inicialmente, utilizadores sem login ou que não pertenciam ao grupo correto conseguiam contornar a falta de botões visíveis digitando o caminho direto no browser (ex: `/portfolio/projeto/novo/`).
* **Surgimento de Tokens Inválidos:** Durante os primeiros testes com o Link Mágico, o browser acusava que o token tinha expirado ou era inválido no momento do clique, falhando o login automático.

## 3. Como Foram Resolvidas (Correcoes)
* **Registo de Namespaces nas URLs:** Resolvi o erro de `NoReverseMatch` adicionando a linha `app_name = 'artigos'` no `urls.py` da app e incluindo a rota com `include('artigos.urls')` no ficheiro de caminhos principal do projeto.
* **Substituição de Atributos do Django:** Corrigi o crash do modelo alterando o argumento inválido `upload_url` para o padrão correto do Django, que é `upload_to='artigos/'`.
* **Proteção de Views no Backend:** Bloqueei o acesso forçado por URL adicionando o decorador `@login_required` no topo de todas as views de escrita/remoção no ficheiro `views.py`.
* **Correção da Descodificação do Token:** Corrigi a view do Link Mágico assegurando o uso de `force_str` e `urlsafe_base64_decode` para traduzir o ID do utilizador corretamente antes de validar o token contra a base de dados.
* **Filtros Contextuais no HTML:** Usei condicionais complexas nos templates (`{% if request.user.is_authenticated and request.user.groups.all.0.name == "gestor-portfolio" %}`) para ocultar completamente elementos visuais de gestão a utilizadores comuns.

## 4. Justificação Técnico-Pedagógica (Justificacao)
* A divisão entre o grupo `gestor-portfolio` (administração do portfólio) e o grupo `autores` (utilizadores comuns que escrevem artigos) foi desenhada para simular um ambiente real de permissões multinível (RBAC - Role-Based Access Control).
* O desenvolvimento do Link Mágico demonstrou como utilizar ferramentas de criptografia e tokens temporários nativos do Django para elevar a experiência de utilização sem comprometer a segurança do servidor.

## 5. Uso de Inteligência Artificial (usoAI)
* **Sim.** Utilizei a IA para compreender o funcionamento dos geradores de tokens do Django, estruturar a lógica de codificação de IDs em Base64 e desenhar o fluxo de herança nos templates para fundir os botões de comentário e gostos sem quebrar o layout limpo preexistente.