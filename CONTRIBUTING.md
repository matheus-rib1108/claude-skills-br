# Como contribuir

Obrigado por querer ajudar. Dá para contribuir de três jeitos:

1. **Dar nota a uma skill**: [formulário de avaliação](../../issues/new?template=avaliar-skill.yml).
2. **Sugerir uma skill**: [formulário de sugestão](../../issues/new?template=sugerir-skill.yml).
3. **Enviar uma skill pronta ou uma melhoria**: abra um Pull Request.

## Enviando uma skill

1. Faça um fork e crie a pasta `skills/<nome-da-skill>/` com o `SKILL.md`. Veja o modelo em [DICAS.md](DICAS.md#criando-a-sua-skill).
2. Adicione a skill em `scripts/skills-meta.json`, com categoria, título, resumo, o que muda, exemplos, antes/depois e dicas.
3. Rode `python scripts/build.py <seu-usuario>` para gerar a página da skill e os zips, e confira se não deu erro.
4. Abra o Pull Request explicando para que serve e como você testou.

## Regras

- Texto em português do Brasil, simples e direto.
- Só conteúdo seu. Skill de outra pessoa entra no [CATALOGO.md](CATALOGO.md) como link, nunca copiada.
- Nada de chaves, senhas, tokens ou dados pessoais.
- Scripts só com bibliotecas conhecidas, sem baixar ou rodar código de fora sem avisar o usuário.
- Ações com efeito fora do computador (enviar mensagem, publicar, comprar) sempre pedem confirmação do usuário.
