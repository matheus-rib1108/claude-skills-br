# Dicas

## Usando as skills

1. **Peça do seu jeito.** Não precisa dizer "use a skill X". Se a descrição combinar com o pedido, o Claude usa sozinho. Se não usar, aí sim diga o nome.
2. **Dê o contexto que a skill pede.** Cada página de skill tem exemplos de pedido. Pedidos com cidade, prazo, público e uma foto rendem muito mais.
3. **Combine skills.** Algumas sequências boas:
   - Vender para o comércio local: `prospeccao-local-br` → `abordagem-whatsapp-vendas` → `orcamento-servicos` → `cardapio-digital` → `site-fortress` → `legal-compliance`.
   - Estudar para prova: `organizador-de-estudos` → `revisao-flashcards` → `matematica-passo-a-passo` ou `tutor-sql`.
   - Cliente de Instagram: `legenda-instagram-negocio` + `photo-editor` + `video-maker` + `humanizar-texto-pt`.
4. **Desligue o que não usa.** No claude.ai, a chave de cada skill fica em Configurações → Capacidades. Menos skills ligadas significa menos confusão na hora de escolher.
5. **Confira o que importa.** Preços, leis e dados mudam. As skills mandam o Claude pesquisar e citar a data, mas vale olhar a fonte antes de mandar para um cliente.

## Criando a sua skill

Uma skill mínima é uma pasta com um `SKILL.md`:

```markdown
---
name: minha-skill
description: O que ela faz em uma frase. Use quando o usuário pedir X, falar de Y ou mandar Z.
---

# Minha skill

## Passo a passo
1. ...
2. ...

## Regras
- ...
```

**Regras que fazem diferença**
- `name`: só letras minúsculas, números e hífens, igual ao nome da pasta.
- `description` é o que decide se a skill ativa. Diga **o que faz** e **quando usar**, com as palavras que você mesmo usaria no pedido ("cardápio", "QR code", "pedido pelo WhatsApp").
- Seja específico. "Escreva bem" não ajuda. "No máximo 5 linhas, uma pergunta no final" ajuda.
- Coloque só o essencial no `SKILL.md`. Material longo vai em arquivos ao lado (`referencia.md`, `scripts/`), e o Claude abre quando precisar.
- Teste com 3 pedidos diferentes antes de publicar.

Para criar com ajuda, instale a [skill-creator da Anthropic](https://github.com/anthropics/skills/tree/main/skills/skill-creator) e peça: "cria uma skill que...".

## Segurança

- Leia o `SKILL.md` e os scripts antes de instalar qualquer skill.
- Desconfie de skill que pede senha, token ou que manda dados para um site.
- Nunca coloque chaves, senhas ou dados de clientes dentro de uma skill que você vai publicar.
