# Assistente de voz (JARVIS)

> Categoria: **Sites e programação** · nome técnico: `assistente-voz-jarvis`

**[⬇ Baixar esta skill (.zip)](https://github.com/matheus-rib1108/claude-skills-br/raw/main/dist/assistente-voz-jarvis.zip)** · [Ver o SKILL.md](SKILL.md) · [Voltar para todas](../../README.md)

## O que faz
Guia para construir seu assistente pessoal de voz em Python: palavra de ativação, transcrição, resposta da IA, voz e comandos no PC.

## O que muda no seu Claude
O Claude monta o projeto em etapas testáveis (texto, depois voz, depois hotword) e pede confirmação para ações perigosas.

| Sem a skill | Com a skill |
|---|---|
| Um código gigante que não roda. | Módulos separados, cada etapa testada antes da próxima. |

## Exemplos de pedido
- "Começa meu JARVIS do zero"
- "Adiciona a palavra de ativação"
- "Faz ele abrir programas no PC"

Você não precisa citar o nome da skill: o Claude lê a descrição e usa sozinho quando o assunto aparece.

## Dicas
- Nunca suba o .env com chaves para o GitHub.
- Para publicar, escolha um nome próprio: JARVIS é marca registrada.

## Como instalar só esta
- **claude.ai ou app**: baixe o zip acima → Configurações → Capacidades → Skills → enviar o arquivo.
- **Claude Code**: descompacte em `~/.claude/skills/` (fica `~/.claude/skills/assistente-voz-jarvis/SKILL.md`).

Passo a passo com imagens: [COMO-INSTALAR.md](../../COMO-INSTALAR.md).

## Arquivos
- `SKILL.md`

## Gostou ou achou um problema?
[Dar nota](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=avaliar-skill.yml&title=%5BNota%5D+assistente-voz-jarvis) · [Relatar problema](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=problema.yml&title=%5BProblema%5D+assistente-voz-jarvis)
