"""Gera docs/images/mapa-skills.svg a partir de scripts/skills-meta.json."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
meta = json.loads((ROOT / "scripts" / "skills-meta.json").read_text(encoding="utf-8"))
cores = ["#C2502E", "#2F6B4F", "#3B5B8C", "#8A5A9E", "#B07A1E", "#4E7C8A", "#6B6B2F", "#A33B5B"]

col_w, gap, x0, y0 = 220, 16, 40, 100
cols = 4
grupos = [(c, [n for n, m in meta["skills"].items() if m["categoria"] == c]) for c in meta["categorias"]]
grupos = [g for g in grupos if g[1]]

partes, alturas = [], [y0] * cols
for i, (cat, nomes) in enumerate(grupos):
    c = min(range(cols), key=lambda k: alturas[k])
    x, y = x0 + c * (col_w + gap), alturas[c]
    h = 44 + 24 * len(nomes)
    cor = cores[i % len(cores)]
    partes.append(f'<rect x="{x}" y="{y}" width="{col_w}" height="{h}" rx="12" fill="#FFFDF8" stroke="#D8CDBB"/>')
    partes.append(f'<rect x="{x}" y="{y}" width="6" height="{h}" rx="3" fill="{cor}"/>')
    partes.append(f'<text x="{x + 18}" y="{y + 28}" class="t">{escape(cat)}</text>')
    for j, n in enumerate(nomes):
        partes.append(f'<text x="{x + 18}" y="{y + 54 + 24 * j}" class="s">{escape(meta["skills"][n]["titulo"])}</text>')
    alturas[c] = y + h + gap

H = max(alturas) + 24
W = x0 * 2 + cols * col_w + (cols - 1) * gap
total = len(meta["skills"])
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t">
  <title id="t">Mapa das {total} skills por categoria</title>
  <style>text{{font-family:"Segoe UI",Roboto,Helvetica,Arial,sans-serif;fill:#1F1B16}}.h{{font-size:22px;font-weight:700}}.t{{font-size:15px;font-weight:700}}.s{{font-size:14px}}</style>
  <rect width="{W}" height="{H}" fill="#F6F1E7"/>
  <text x="{x0}" y="56" class="h">Mapa das {total} skills</text>
  {"".join(partes)}
</svg>
'''
(ROOT / "docs" / "images" / "mapa-skills.svg").write_text(svg, encoding="utf-8", newline="\n")
print(W, H)
