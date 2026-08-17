# MCP Plugins

Marketplace publica de plugins Codex e Cursor dos projetos de Cadu Osmarini.

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
- `sapiens-mcp`: consulta segura ao dicionario e banco Sapiens via MCP local com OAuth.

Para usar `sapiens-mcp`, inicie antes o servidor no projeto correspondente:

```bash
cd /home/carlos/sapiens-mcp
pnpm run start:http
```

Depois instale o plugin:

```bash
codex plugin add sapiens-mcp@mcp-plugins
```

## Cursor

No Cursor, abra **Settings → Plugins → Marketplaces**, importe o repositório:

```text
https://github.com/caduosmarini/mcp-plugins
```

Depois instale **Casa Finance** e/ou **Sapiens MCP**. Se o servidor pedir login, conclua o OAuth em **Settings → Tools & MCP**.

Como alternativa, adicione os servidores direto em `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "casa-finance": {
      "type": "http",
      "url": "https://casa.osmariniziliotto.com.br/finance/mcp"
    },
    "sapiens-mcp": {
      "type": "http",
      "url": "https://sapiens-mcp.osmariniziliotto.com.br/mcp"
    }
  }
}
```

## Estrutura

```text
.agents/plugins/marketplace.json
.cursor-plugin/marketplace.json
plugins/
  casa-finance/
    .codex-plugin/plugin.json
    .cursor-plugin/plugin.json
    .mcp.json
    mcp.json
  sapiens-mcp/
    .codex-plugin/plugin.json
    .cursor-plugin/plugin.json
    .mcp.json
    mcp.json
```

Cada plugin fica isolado em `plugins/<nome>`. O Codex lê `.agents/plugins/marketplace.json`; o Cursor lê `.cursor-plugin/marketplace.json`.
