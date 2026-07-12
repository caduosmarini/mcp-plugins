# MCP Plugins

Marketplace publica de plugins Codex dos projetos de Cadu Osmarini.

## Instalar no Codex

Adicione esta marketplace:

```bash
codex plugin marketplace add git@github.com:caduosmarini/mcp-plugins.git
```

Depois instale o plugin desejado:

```bash
codex plugin add casa-finance@mcp-plugins
```

Na primeira conexao, o Codex abrira o fluxo de autenticacao do Casa.

## Plugins disponiveis

- `casa-finance`: acesso de leitura e escrita ao Finance do projeto Casa via MCP.

## Estrutura

```text
.agents/plugins/marketplace.json
plugins/
  casa-finance/
    .codex-plugin/plugin.json
    .mcp.json
```

Cada plugin fica isolado em `plugins/<nome>` e e publicado pelo catalogo em `.agents/plugins/marketplace.json`.
