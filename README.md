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

- `moveis`: skill de projetos de móveis sob medida, com 3D, cortes, bordas, ferragens, LEDs, orçamento e publicação opcional. Não requer servidor MCP próprio.
- `casa-finance`: acesso de leitura e escrita ao Finance do projeto Casa via MCP.
- `sapiens-mcp`: consulta segura ao dicionario e banco Sapiens via MCP, com prompts de dominio e caderno de descobertas.

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

## Móveis sob medida

O plugin `moveis` contém a skill `projetar-moveis`. Exemplos: projetar uma estante a partir de fotos, revisar a profundidade de um armário e sincronizar documentos, ou incluir LEDs e ferragens.

```bash
codex plugin add moveis@mcp-plugins
```

A skill funciona com as ferramentas disponíveis no ambiente. Para todos os artefatos, usa Python, um modelador/exportador GLB (por exemplo Blender), bibliotecas de PDF/XLSX e um navegador para teste. A publicação requer Sites disponível e autorização para o destino e público. O plugin não instala essas dependências nem contém um servidor MCP. Inclui um exemplo sintético e um validador dimensional em `plugins/moveis/skills/projetar-moveis`.

```bash
python3 plugins/moveis/skills/projetar-moveis/scripts/validate_project.py plugins/moveis/skills/projetar-moveis/assets/exemplo-minimo.json
```
