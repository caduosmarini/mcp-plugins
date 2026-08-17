---
name: scrum-finalizar-tarefa
description: Validar e finalizar uma task do Conecta Scrum, conferindo o escopo Git, criando commit, comentando a entrega, movendo para Validar Sandbox e registrando o tempo. Usar quando o usuário pedir para finalizar, concluir, fechar ou entregar uma task em andamento.
---

# Finalizar tarefa Scrum

Usar as ferramentas MCP do plugin Conecta e seguir o workflow do prompt MCP `scrum-finalizar-tarefa`.

## Fluxo

1. Identificar o `full_id`, conferir a task, sua spec e o escopo atual do Git.
2. Comparar a entrega com os Critérios de Aceite e executar as validações focadas. Corrigir falhas pertencentes ao escopo antes de finalizar.
3. Atualizar a spec para refletir o que foi comprovadamente entregue.
4. Incluir apenas arquivos da task e criar commit no padrão `feat(<full_id>): <resumo em pt-BR>`. Não criar commit vazio.
5. Comentar na task o que foi feito, abordagem, validações, commits e caminho da spec.
6. Consultar os estados e mover para a correspondência inequívoca de `Validar Sandbox`.
7. Consultar o timer. Se estiver na mesma task, parar sem duplicar o registro; se estiver em outra, não interromper sem confirmação; se não houver timer, obter duração ou intervalo e registrar manualmente.
8. Informar estado final, commits, testes, spec, tempo e qualquer pendência real.

## Regras

- Usar o `full_id` legível nas ferramentas e no escopo do commit.
- Preservar alterações não relacionadas e não incluí-las no commit.
- Não declarar a task pronta com testes falhando ou Critérios de Aceite pendentes.
- Não fazer push nem abrir PR sem pedido explícito.
- Se o host disponibilizar diretamente o prompt MCP `scrum-finalizar-tarefa`, preferir seu conteúdo atual em caso de divergência.
