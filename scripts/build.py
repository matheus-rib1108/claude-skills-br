"""Gera as páginas de cada skill, os zips em dist/, o marketplace e a tabela do README.

Uso: python scripts/build.py <usuario-do-github>
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
REPO = "claude-skills-br"


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit(f"{path}: sem frontmatter")
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    name = data.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        raise SystemExit(f"{path}: name inválido: {name!r}")
    if name != path.parent.name:
        raise SystemExit(f"{path}: name {name!r} diferente da pasta")
    if not data.get("description") or len(data["description"]) > 1024:
        raise SystemExit(f"{path}: description ausente ou maior que 1024")
    return data


def skill_readme(name, m, owner):
    raw = f"https://github.com/{owner}/{REPO}/raw/main/dist/{name}.zip"
    exemplos = "\n".join(f"- \"{e}\"" for e in m["exemplos"])
    dicas = "\n".join(f"- {d}" for d in m["dicas"])
    arquivos = sorted(p.relative_to(SKILLS / name).as_posix()
                      for p in (SKILLS / name).rglob("*") if p.is_file() and p.name != "README.md")
    lista = "\n".join(f"- `{a}`" for a in arquivos)
    return f"""# {m['titulo']}

> Categoria: **{m['categoria']}** · nome técnico: `{name}`

**[⬇ Baixar esta skill (.zip)]({raw})** · [Ver o SKILL.md](SKILL.md) · [Voltar para todas](../../README.md)

## O que faz
{m['resumo']}

## O que muda no seu Claude
{m['muda']}

| Sem a skill | Com a skill |
|---|---|
| {m['antes']} | {m['depois']} |

## Exemplos de pedido
{exemplos}

Você não precisa citar o nome da skill: o Claude lê a descrição e usa sozinho quando o assunto aparece.

## Dicas
{dicas}

## Como instalar só esta
- **claude.ai ou app**: baixe o zip acima → Configurações → Capacidades → Skills → enviar o arquivo.
- **Claude Code**: descompacte em `~/.claude/skills/` (fica `~/.claude/skills/{name}/SKILL.md`).

Passo a passo com imagens: [COMO-INSTALAR.md](../../COMO-INSTALAR.md).

## Arquivos
{lista}

## Gostou ou achou um problema?
[Dar nota](https://github.com/{owner}/{REPO}/issues/new?template=avaliar-skill.yml&title=%5BNota%5D+{name}) · [Relatar problema](https://github.com/{owner}/{REPO}/issues/new?template=problema.yml&title=%5BProblema%5D+{name})
"""


def zip_dir(target, folders):
    with zipfile.ZipFile(target, "w", zipfile.ZIP_STORED) as z:
        for folder in folders:
            for p in sorted(folder.rglob("*"), key=lambda q: q.as_posix()):
                if p.is_file() and "__pycache__" not in p.parts:
                    info = zipfile.ZipInfo(p.relative_to(folder.parent).as_posix(), (2026, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_STORED
                    info.create_system = 3  # igual no Windows e no Linux
                    info.external_attr = 0o644 << 16
                    z.writestr(info, p.read_bytes())


def main():
    owner = sys.argv[1] if len(sys.argv) > 1 else "SEU-USUARIO"
    meta = json.loads((ROOT / "scripts" / "skills-meta.json").read_text(encoding="utf-8"))
    folders = sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())
    names = [p.name for p in folders]
    missing = set(names) ^ set(meta["skills"])
    if missing:
        raise SystemExit(f"meta e pastas não batem: {sorted(missing)}")

    for p in folders:
        frontmatter(p / "SKILL.md")
        (p / "README.md").write_text(skill_readme(p.name, meta["skills"][p.name], owner), encoding="utf-8", newline="\n")

    DIST.mkdir(exist_ok=True)
    for old in DIST.glob("*.zip"):
        old.unlink()
    for p in folders:
        zip_dir(DIST / f"{p.name}.zip", [p])
    zip_dir(DIST / "todas-as-skills.zip", folders)

    plugin_dir = ROOT / ".claude-plugin"
    plugin_dir.mkdir(exist_ok=True)
    market = {
        "name": REPO,
        "owner": {"name": owner},
        "metadata": {"description": "Skills para Claude em português do Brasil: estudo, vendas locais, redes sociais, sites e segurança.", "version": "1.0.0"},
        "plugins": [{
            "name": "skills-br",
            "description": "Todas as skills do claude-skills-br.",
            "source": "./",
            "strict": False,
            "skills": [f"./skills/{n}" for n in names],
        }],
    }
    (plugin_dir / "marketplace.json").write_text(json.dumps(market, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    rows = []
    for cat in meta["categorias"]:
        itens = [n for n in names if meta["skills"][n]["categoria"] == cat]
        if not itens:
            continue
        rows.append(f"\n### {cat}\n\n| Skill | Para que serve | Baixar |\n|---|---|---|")
        for n in itens:
            m = meta["skills"][n]
            rows.append(f"| [{m['titulo']}](skills/{n}/README.md) | {m['resumo']} | [zip](https://github.com/{owner}/{REPO}/raw/main/dist/{n}.zip) |")
    table = "\n".join(rows).strip()
    readme = ROOT / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        text = re.sub(r"(<!-- TABELA:INICIO -->).*?(<!-- TABELA:FIM -->)", lambda m: f"{m.group(1)}\n{table}\n{m.group(2)}", text, flags=re.S)
        text = text.replace("SEU-USUARIO", owner)
        readme.write_text(text, encoding="utf-8", newline="\n")
    print(f"{len(names)} skills, {len(names) + 1} zips")


if __name__ == "__main__":
    main()
