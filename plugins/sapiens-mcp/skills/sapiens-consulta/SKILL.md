---
name: sapiens-consulta
description: Consulta somente leitura ao ERP Sapiens. Use ao localizar tabelas, campos, dados, regras de consulta ou aprendizados no Sapiens/Senior.
---

# Consulta Sapiens

Sempre usar o servidor MCP `sapiens-mcp`. Não inventar tabelas, joins, significados de código nem fórmulas de total.

O cliente **não carrega** os prompts do MCP sozinho. Não basta ver o nome `sapiens-consultar-faturamento` na descrição. Chamar a tool `get_prompt`.

## Obrigatório antes de consultar

1. `list_prompts` se houver dúvida do domínio; em seguida `get_prompt` com o nome ou apelido (`faturamento`, `contratos`, `notas-fiscais`, `pedidos`, `clientes`, `financeiro`, `produtos-estoque`, `banco`).
2. `search_notes` no mesmo domínio/tabela.
3. Só então `search_schema` → `describe_table` → `find_columns` → `validate_select` → `execute_select`.

`describe_table` já devolve o corpo do prompt de domínio e as notas ligadas à tabela. Mesmo assim, para faturamento, contratos, notas e totais, chamar `get_prompt` — lá está o SQL modelo e as regras que o catálogo não confirma (`SitNfv`, `TipNfs`, `VlrBpr`, etc.).

## Prompts

- `sapiens-consultar-banco`
- `sapiens-consultar-clientes`
- `sapiens-consultar-contratos`
- `sapiens-consultar-pedidos`
- `sapiens-consultar-produtos-estoque`
- `sapiens-consultar-notas-fiscais`
- `sapiens-consultar-faturamento`
- `sapiens-consultar-financeiro`

## Caderno

Quando descobrir o jeito certo, `save_note` (título + texto; domínio, tabelas e SQL se couber).

Documentação oficial: https://documentacao.senior.com.br
