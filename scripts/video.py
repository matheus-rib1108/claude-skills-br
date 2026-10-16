"""Gera docs/videos/demo.mp4 e demo.gif só com ffmpeg (filtro drawtext).

Uso: python scripts/video.py
Precisa do ffmpeg no PATH. Fontes: Segoe UI (Windows) ou DejaVu Sans (Linux).
"""
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "videos"
W, H, CENA = 1280, 720, 4.0
FUNDO, TINTA, CINZA, DESTAQUE = "0xF6F1E7", "0x1F1B16", "0x5A5248", "0xC2502E"

CENAS = [
    [("claude-skills-br", 72, TINTA, True), ("29 skills para o Claude, em português", 36, CINZA, False)],
    [("1. Escolha", 60, DESTAQUE, True), ("Uma skill só ou todas de uma vez", 38, TINTA, False), ("dist/todas-as-skills.zip", 32, CINZA, False)],
    [("2. Instale", 60, DESTAQUE, True), ("claude.ai: Configurações > Capacidades > Skills", 34, TINTA, False), ("Claude Code: pasta ~/.claude/skills/", 34, TINTA, False)],
    [("3. Peça normalmente", 60, DESTAQUE, True), ("\u201cFaz o cardápio digital da pizzaria\u201d", 38, TINTA, False), ("A skill cardapio-digital entra sozinha", 32, CINZA, False)],
    [("Avalie e sugira", 60, DESTAQUE, True), ("Dê nota de 1 a 5 e peça skills novas", 38, TINTA, False), ("nas Issues do repositório", 32, CINZA, False)],
]


def fonte(negrito):
    candidatos = (["C:/Windows/Fonts/segoeuib.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"] if negrito
                  else ["C:/Windows/Fonts/segoeui.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"])
    for c in candidatos:
        if Path(c).exists():
            return c.replace(":", "\\:")
    raise SystemExit("fonte não encontrada")


def main():
    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg não encontrado")
    OUT.mkdir(parents=True, exist_ok=True)
    total = CENA * len(CENAS)
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        filtros = []
        for i, linhas in enumerate(CENAS):
            ini, fim = i * CENA, (i + 1) * CENA
            alpha = f"if(lt(t,{ini}+0.4),(t-{ini})/0.4,if(gt(t,{fim}-0.4),({fim}-t)/0.4,1))"
            altura = sum(tam * 1.6 for _, tam, _, _ in linhas)
            y = (H - altura) / 2
            for j, (texto, tam, cor, negrito) in enumerate(linhas):
                arq = tmp / f"t{i}_{j}.txt"
                arq.write_text(texto, encoding="utf-8")
                caminho = arq.as_posix().replace(":", "\\:")
                filtros.append(
                    f"drawtext=fontfile='{fonte(negrito)}':textfile='{caminho}':fontsize={tam}:fontcolor={cor}"
                    f":x=(w-text_w)/2:y={y:.0f}:alpha='{alpha}':enable='between(t,{ini},{fim})'"
                )
                y += tam * 1.6
        filtros.append(f"drawbox=x=0:y={H - 10}:w=iw*t/{total}:h=10:color={DESTAQUE}:t=fill")
        script = tmp / "filtro.txt"
        script.write_text(",\n".join(filtros), encoding="utf-8")
        mp4, gif = OUT / "demo.mp4", OUT / "demo.gif"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", f"color=c={FUNDO}:s={W}x{H}:d={total}:r=30",
                        "-/vf", str(script), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(mp4)], check=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(mp4), "-vf",
                        "fps=10,scale=720:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=64[p];[b][p]paletteuse",
                        str(gif)], check=True)
    for f in (mp4, gif):
        print(f.name, f.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
