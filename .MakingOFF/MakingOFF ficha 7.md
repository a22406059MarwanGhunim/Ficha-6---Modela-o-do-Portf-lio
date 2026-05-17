# Making Off - Implementação do Portfólio em Django

Este documento descreve o processo de desenvolvimento, as decisões tomadas e as dificuldades encontradas durante a implementação das interfaces de consulta do projeto Portfólio.

## 1. Descrição das Decisões (DescricaoDescisoes)
Foi decidida a implementação de uma arquitetura **MVT (Model-View-Template)** completa para cada entidade do sistema. Optou-se por criar uma página `home.html` centralizada que serve como ponto de entrada, utilizando uma grelha de botões para facilitar a navegação entre os diferentes modelos (Licenciatura, UCs, Projetos, Tecnologias, etc.). Para manter a consistência visual, foi implementado um ficheiro `base.html` que contém o layout comum e o menu de navegação.

## 2. Dificuldades e Erros Encontrados (Erros)
* **Erro 404 na Raiz:** Ao iniciar o servidor, a página inicial não estava definida, resultando num erro de "Page Not Found" no endereço `localhost:8000/`.
* **TemplateDoesNotExist:** Inicialmente, houve confusão na estrutura de pastas necessária para o Django encontrar os templates dentro da aplicação `portfolio`.
* **Mapeamento de Nomes:** Pequenas discrepâncias entre os nomes das classes no `models.py` (ex: `UC` vs `Disciplina`) e a sua chamada nas views.

## 3. Correções Efetuadas (Correcoes)
* Configuração do `project/urls.py` para incluir as URLs da aplicação `portfolio` e definição de um `RedirectView` ou rota vazia para a página `home`.
* Reorganização da estrutura de pastas para `portfolio/templates/portfolio/*.html`.
* Revisão rigorosa dos campos dos modelos para garantir que as tags do Django Template (`{{ tecnologia.nome }}`) correspondiam exatamente aos atributos definidos nas classes.

## 4. Justificação (Justificacao)
A estrutura modular adotada permite uma manutenção mais simples e uma expansão futura facilitada. A escolha de separar cada modelo numa view dedicada garante que o utilizador tenha uma visão clara e organizada de cada componente do percurso académico, cumprindo os requisitos pedagógicos da ficha de trabalho.

## 5. Uso de Inteligência Artificial (usoAI)
* **Sim.** Foi utilizada a assistência de IA para a geração do código base do html e debugging do código para a resolução dos problemas referidos no ponto 2.
