# Editor de fotos

> Categoria: **Redes sociais, foto e vídeo** · nome técnico: `photo-editor`

**[⬇ Baixar esta skill (.zip)](https://github.com/matheus-rib1108/claude-skills-br/raw/main/dist/photo-editor.zip)** · [Ver o SKILL.md](SKILL.md) · [Voltar para todas](../../README.md)

## O que faz
Melhora fotos no seu computador: luz, cor, nitidez, ampliação com IA, remoção de fundo e recorte para Instagram ou site.

## O que muda no seu Claude
O Claude edita a foto de verdade com Python (Pillow, OpenCV, rembg) e mostra antes e depois.

| Sem a skill | Com a skill |
|---|---|
| Dicas de como editar no celular. | Arquivo editado pronto, com comparação antes/depois. |

## Exemplos de pedido
- "Melhora essa foto da pizza para o Instagram"
- "Tira o fundo do produto"
- "Recorta em 4:5 para o feed"

Você não precisa citar o nome da skill: o Claude lê a descrição e usa sozinho quando o assunto aparece.

## Dicas
- Instale uma vez: pip install pillow opencv-contrib-python-headless numpy rembg onnxruntime
- Fotos com boa luz natural rendem mais que qualquer filtro.

## Como instalar só esta
- **claude.ai ou app**: baixe o zip acima → Configurações → Capacidades → Skills → enviar o arquivo.
- **Claude Code**: descompacte em `~/.claude/skills/` (fica `~/.claude/skills/photo-editor/SKILL.md`).

Passo a passo com imagens: [COMO-INSTALAR.md](../../COMO-INSTALAR.md).

## Arquivos
- `SKILL.md`
- `scripts/photo.py`

## Gostou ou achou um problema?
[Dar nota](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=avaliar-skill.yml&title=%5BNota%5D+photo-editor) · [Relatar problema](https://github.com/matheus-rib1108/claude-skills-br/issues/new?template=problema.yml&title=%5BProblema%5D+photo-editor)
