---
name: scrum-iniciar-tarefa
description: Iniciar e executar uma task existente do Conecta Scrum, cuidando do timer, spec, pré-condições, estado, planejamento e implementação. Usar quando o usuário pedir para iniciar, começar, pegar ou executar uma task identificada por full_id como CON-123.
---

# Iniciar tarefa Scrum

Usar as ferramentas MCP do plugin Conecta e seguir o workflow do prompt MCP `scrum-iniciar-tarefa`.

## Fluxo

1. Consultar o timer. Iniciar na task se estiver livre; manter se já estiver nela; pedir decisão antes de trocar de outra task; vincular se estiver ativo sem task.
2. Ler a task e extrair título, descrição, prioridade, tipo, sprint, estado, responsável, dependências, subtasks e comentários.
3. Procurar `docs/specs/<full_id>-*.md`, com fallback `docs/specs/<full_id>.md`. Se não existir, criar a spec a partir da task, sem inventar Objetivo ou Critérios de Aceite, e atualizar a descrição com seu caminho.
4. Confirmar com o usuário somente a spec criada ou informações essenciais que precisaram ser elicitadas.
5. Validar dependências bloqueantes e responsável. Pedir autorização antes de ignorar bloqueio ou autoatribuir a task.
6. Se necessário, localizar o estado inequívoco `Em Andamento` e mover a task.
7. Explorar o código, montar a TODO técnica baseada na spec e seguir sem pedir uma nova aprovação do plano.
8. Criar o comentário inicial com estado, timer, caminho da spec e plano resumido.
9. Implementar os Critérios de Aceite, mantendo a spec e os comentários atualizados quando houver mudança relevante.
10. Parar antes de commit, movimentação final e encerramento do tempo; isso pertence a `scrum-finalizar-tarefa`.

## Regras

- Usar o `full_id` legível nas ferramentas, nunca o ID numérico interno.
- Não misturar o tempo de duas tasks.
- Não ignorar dependências nem trocar responsável silenciosamente.
- Não executar comandos destrutivos de banco.
- Se o host disponibilizar diretamente o prompt MCP `scrum-iniciar-tarefa`, preferir seu conteúdo atual em caso de divergência.
