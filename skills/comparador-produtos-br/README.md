# Comparador de produtos

> Categoria: **Vendas e negócio local** · nome técnico: `comparador-produtos-br`

**[⬇ Baixar esta skill (.zip)](https://github.com/matheus-rib1108/claude-skills-br/raw/main/dist/comparador-produtos-br.zip)** · [Ver o SKILL.md](SKILL.md) · [Voltar para todas](../../README.md)

## O que faz
Compara produtos de lojas brasileiras (Pichau, Kabum, Terabyte, Amazon, Mercado Livre) com tabela, ranking e link certo.

## O que muda no seu Claude
O Claude define critérios antes, abre a página da loja para confirmar preço e confere se o link leva ao modelo certo.

| Sem a skill | Com a skill |
|---|---|
| Opiniões genéricas e preço de memória. | Veredito, tabela por critério, top 3 com preço PIX consultado na data e alertas. |

## Exemplos de pedido
- "Qual a melhor cadeira gamer até R$ 1.200 na Pichau?"
- "Compara esses 3 headsets (print)"
- "Top 5 SSD custo-benefício"

Você não precisa citar o nome da skill: o Claude lê a descrição e usa sozinho quando o assunto aparece.

## Dicas
- Diga quanto tempo usa por dia e para quê.
- Preço muda: confira a data da consulta.

## Como instalar só esta
- **claude.ai ou app**: baixe o zip acima → Configurações → Capacidades → Skills → enviar o arquivo.
- **Claude Code**: descompacte em `~/.claude/skills/` (fica `~/.claude/skills/comparador-produtos-br/SKILL.md`).

Passo a passo com imagens: [COMO-INSTALAR.md](../../COMO-INSTALAR.md).

## Arquivos
- `SKILL.md`

## Gostou ou achou um problema?
[Dar nota](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=avaliar-skill.yml&title=%5BNota%5D+comparador-produtos-br) · [Relatar problema](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=problema.yml&title=%5BProblema%5D+comparador-produtos-br)
