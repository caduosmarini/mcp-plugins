---
name: scrum-criar-task
description: Criar uma task no Conecta Scrum a partir de um pedido em linguagem natural, definindo spec, projeto, sprint, responsável e estimativa. Usar quando o usuário pedir para criar, abrir ou registrar uma task futura no Scrum.
---

# Criar task Scrum

Usar as ferramentas MCP do plugin Conecta e seguir o workflow do prompt MCP `scrum-criar-task`.

## Fluxo

1. Extrair do pedido o Objetivo e pelo menos dois Critérios de Aceite verificáveis. Perguntar somente pelas lacunas essenciais e obter confirmação da spec antes da criação.
2. Consultar projetos e apresentar as sprints ativas, sempre incluindo `Backlog (sem sprint)`.
3. Consultar tipos, prioridades e estados. Usar `Backlog` sem sprint e `A Fazer` com sprint; inferir tipo e usar prioridade `Média` quando não houver urgência.
4. Apresentar a equipe, sugerir `Eu mesmo` e confirmar o responsável.
5. Propor e confirmar a estimativa em minutos.
6. Criar a task com descrição curta em Markdown contendo Objetivo, Critérios de Aceite e referência à spec completa.
7. Criar `docs/specs/<full_id>-<slug>.md`, fazer um commit exclusivo da spec (`docs(<full_id>): adiciona spec da task`), atualizar a descrição da task com o caminho real e comentar a publicação com o hash.
8. Perguntar o tempo gasto na elicitação e registrá-lo somente com autorização.
9. Informar `full_id`, link, spec, projeto, sprint/estado, responsável, estimativa e tempo.

## Regras

- Usar o `full_id` legível nas ferramentas, nunca o ID numérico interno.
- Não inventar Objetivo nem Critérios de Aceite.
- Usar Markdown puro.
- Não implementar a task neste fluxo. A spec deve ser commitada antes de concluir a criação da task, incluindo somente seu próprio arquivo.
- Se o host disponibilizar diretamente o prompt MCP `scrum-criar-task`, preferir seu conteúdo atual em caso de divergência.
