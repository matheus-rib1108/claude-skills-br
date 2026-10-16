# Fortaleza do site

> Categoria: **Segurança e lei** · nome técnico: `site-fortress`

**[⬇ Baixar esta skill (.zip)](https://github.com/matheus-rib1108/claude-skills-br/raw/main/dist/site-fortress.zip)** · [Ver o SKILL.md](SKILL.md) · [Voltar para todas](../../README.md)

## O que faz
Auditoria de segurança completa do seu próprio site em 12 fases: segredos, dependências, login, pagamentos, cabeçalhos, LGPD. Corrige e prova cada correção.

## O que muda no seu Claude
O Claude testa o site como um atacante faria (só no que é seu), corrige o que achar e mostra a prova de que ficou seguro.

| Sem a skill | Com a skill |
|---|---|
| "Parece seguro." | Relatório fase por fase com o que foi achado, corrigido e verificado. |

## Exemplos de pedido
- "Deixa o site da pizzaria seguro antes de publicar"
- "Testa meu login como hacker"
- "Verifica se o pagamento está certo"

Você não precisa citar o nome da skill: o Claude lê a descrição e usa sozinho quando o assunto aparece.

## Dicas
- Rode antes de todo lançamento e depois de mudanças grandes.
- Só use em sites que são seus.

## Como instalar só esta
- **claude.ai ou app**: baixe o zip acima → Configurações → Capacidades → Skills → enviar o arquivo.
- **Claude Code**: descompacte em `~/.claude/skills/` (fica `~/.claude/skills/site-fortress/SKILL.md`).

Passo a passo com imagens: [COMO-INSTALAR.md](../../COMO-INSTALAR.md).

## Arquivos
- `SKILL.md`

## Gostou ou achou um problema?
[Dar nota](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=avaliar-skill.yml&title=%5BNota%5D+site-fortress) · [Relatar problema](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=problema.yml&title=%5BProblema%5D+site-fortress)
