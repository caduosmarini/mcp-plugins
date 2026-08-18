---
name: sapiens-consulta
description: Consulta somente leitura ao ERP Sapiens. Use ao localizar tabelas, campos, dados, regras de consulta ou aprendizados no Sapiens/Senior.
---

# Consulta Sapiens

Sempre usar o servidor MCP `sapiens-mcp` e os **prompts que ele serve**. Não inventar tabelas, joins nem regras de negócio.

## Prompts do MCP

Escolher o prompt pelo assunto antes de montar SQL:

- `sapiens-consultar-banco` — descoberta genérica de esquema
- `sapiens-consultar-clientes`
- `sapiens-consultar-contratos`
- `sapiens-consultar-pedidos`
- `sapiens-consultar-produtos-estoque`
- `sapiens-consultar-notas-fiscais`
- `sapiens-consultar-faturamento`
- `sapiens-consultar-financeiro`

## Caderno de descobertas

O MCP guarda aprendizados de consultas anteriores (erros, joins, filtros, jeito certo).

1. Antes de montar o SQL, usar `search_notes` (domínio e/ou tabela). `get_note` se precisar do detalhe.
2. Os prompts de domínio já trazem um resumo das notas daquele assunto.
3. Quando descobrir o jeito certo, gravar na hora com `save_note` (título + texto; domínio, tabelas e SQL se couber).

## Fluxo de consulta

`search_schema` → `describe_table` → `find_columns` → `validate_select` → `execute_select`.

Documentação oficial: https://documentacao.senior.com.br
