# Assistir vídeo por link

> Categoria: **Redes sociais, foto e vídeo** · nome técnico: `video-link`

**[⬇ Baixar esta skill (.zip)](https://github.com/matheus-rib1108/claude-skills-br/raw/main/dist/video-link.zip)** · [Ver o SKILL.md](SKILL.md) · [Voltar para todas](../../README.md)

## O que faz
Você manda o link (Instagram, TikTok, YouTube) e o Claude "assiste": baixa, transcreve a fala e tira quadros da imagem.

## O que muda no seu Claude
O Claude consegue resumir, anotar ou copiar a ideia de um vídeo que antes ele não conseguia ver.

| Sem a skill | Com a skill |
|---|---|
| "Não consigo assistir vídeos." | Transcrição, quadros principais e resumo do vídeo. |

## Exemplos de pedido
- "O que esse reels ensina? (link)"
- "Resume esse vídeo do YouTube em tópicos"
- "Copia a ideia desse TikTok para a pizzaria"

Você não precisa citar o nome da skill: o Claude lê a descrição e usa sozinho quando o assunto aparece.

## Dicas
- Precisa de yt-dlp, faster-whisper e ffmpeg instalados.
- Só use com vídeos públicos ou seus.

## Como instalar só esta
- **claude.ai ou app**: baixe o zip acima → Configurações → Capacidades → Skills → enviar o arquivo.
- **Claude Code**: descompacte em `~/.claude/skills/` (fica `~/.claude/skills/video-link/SKILL.md`).

Passo a passo com imagens: [COMO-INSTALAR.md](../../COMO-INSTALAR.md).

## Arquivos
- `SKILL.md`
- `scripts/watch.py`

## Gostou ou achou um problema?
[Dar nota](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=avaliar-skill.yml&title=%5BNota%5D+video-link) · [Relatar problema](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=problema.yml&title=%5BProblema%5D+video-link)
