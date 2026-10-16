# Catálogo de skills de outras pessoas

Pesquisa feita em 15/10/2026. Aqui só tem **link**: as skills continuam nos repositórios dos autores, com a licença deles. As skills deste repositório estão no [README](README.md).

Abri cada repositório desta lista e confirmei que ele existe. Na maioria, li o README ou a listagem de pastas, e não o `SKILL.md` de cada skill. Leia o `SKILL.md` antes de instalar.

**Como instalar**
- **npx** = `npx skills add <dono>/<repo>`. Só uso quando o [skills.sh](https://skills.sh) lista o repositório, ou quando o README dele aponta para o skills.sh.
- **Cópia** = copiar a pasta da skill para `~/.claude/skills/` (no Windows: `C:\Users\<você>\.claude\skills\`). Muitos READMEs também trazem `/plugin marketplace add ...`. Esse comando vem do autor, não foi conferido por mim.

**Avisos**
- Skills podem rodar código. Leia o `SKILL.md` antes de instalar, principalmente de repositório pequeno.
- `docx`, `pdf`, `pptx` e `xlsx` da Anthropic são "source-available", não open source.
- Quase tudo está em inglês. Para o Claude responder em português, é só pedir.

---

## Estudo

| Skill | Repositório | O que faz | Instalar | Pra quem serve |
|---|---|---|---|---|
| obsidian-notes-creator | [szeyu/vibe-study-skills](https://github.com/szeyu/vibe-study-skills) (Apache-2.0) | Transforma slides, PDFs e anotações em notas de estudo para o Obsidian, com exemplos e diagramas. | Cópia | Quem estuda com Obsidian. |
| teach | [mattpocock/skills](https://github.com/mattpocock/skills) (MIT) | Ensina um conceito em várias sessões. | npx `mattpocock/skills` | Aprender SQL, JavaScript ou Next.js por etapas. |
| grill-me | [mattpocock/skills](https://github.com/mattpocock/skills) (MIT) | O Claude faz perguntas sobre o seu plano até não sobrar dúvida. | npx (mesmo repo) | Validar um projeto antes de começar. |
| wait-what | [mattpocock/skills](https://github.com/mattpocock/skills) (MIT) | Explica de novo, em linguagem simples, uma resposta confusa. | npx (mesmo repo) | Entender mensagens de erro e termos técnicos. |
| research | [mattpocock/skills](https://github.com/mattpocock/skills) (MIT) | Pesquisa em fontes primárias e salva um .md com citações. | npx (mesmo repo) | Trabalho escolar com fontes. |
| learn-this, ship-learn-next, youtube-transcript, article-extractor, unblock-action | [michalparkola/tapestry-skills-for-claude-code](https://github.com/michalparkola/tapestry-skills-for-claude-code) (MIT) | Transformam vídeo, artigo ou PDF em plano de estudo, transcrevem o YouTube, extraem o texto de artigos e quebram tarefas travadas em passos. | Cópia | Estudar por videoaula sem só assistir. |
| claude-scientific-skills | [K-Dense-AI/claude-scientific-skills](https://github.com/K-Dense-AI/claude-scientific-skills) (MIT; cada skill tem licença própria) | 177 skills de biologia, química, física, engenharia e dados. | Cópia | Trabalhos de ciências e desafios técnicos. |

## Programação

| Skill | Repositório | O que faz | Instalar | Pra quem serve |
|---|---|---|---|---|
| mysql | [planetscale/database-skills](https://github.com/planetscale/database-skills) (MIT) | Boas práticas de MySQL: schema, índices, consultas lentas, transações. | npx `planetscale/database-skills` | Quem estuda MySQL. |
| supabase-postgres-best-practices | [supabase/agent-skills](https://github.com/supabase/agent-skills) (MIT) | Postgres: consultas, índices e Row-Level Security. | Cópia | Quem vai do MySQL para o Postgres. |
| neon-postgres, neon-auth | [neondatabase/agent-skills](https://github.com/neondatabase/agent-skills) (Apache-2.0) | Postgres serverless e login gerenciado. | Cópia | Banco e login para sites de clientes. |
| react-best-practices, composition-patterns, react-view-transitions, web-design-guidelines | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) (MIT) | Performance em React/Next.js, componentes limpos, animação entre páginas e revisão de UI. | Cópia | Quem faz sites em Next.js. |
| systematic-debugging, test-driven-development, brainstorming, writing-plans, verification-before-completion | [obra/superpowers](https://github.com/obra/superpowers) (MIT) | Achar a causa do bug, testes primeiro, planejar antes de construir e conferir antes de dizer "pronto". | Cópia | Qualquer projeto de código. |
| diagnosing-bugs, tdd | [mattpocock/skills](https://github.com/mattpocock/skills) (MIT) | Bugs difíceis em fases; TDD uma fatia por vez. | npx `mattpocock/skills` | Complementa o superpowers. |
| playwright-skill | [lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill) (MIT) | O Claude escreve e roda testes no navegador. | Cópia de `skills/playwright-skill/` + `npm run setup` | Testar o site antes de entregar. |
| webapp-testing, mcp-builder, claude-api, skill-creator | [anthropics/skills](https://github.com/anthropics/skills) (Apache-2.0) | Testar app local, criar servidor MCP, usar a API do Claude, criar skills. | Cópia | Sites, assistentes de IA e skills próprias. |
| find-skills | [vercel-labs/skills](https://github.com/vercel-labs/skills) (MIT) | Busca skills pelo terminal (`npx skills find <termo>`). | npx | Descobrir skills novas. |

## Design

| Skill | Repositório | O que faz | Instalar | Pra quem serve |
|---|---|---|---|---|
| frontend-design, canvas-design, algorithmic-art, brand-guidelines, theme-factory | [anthropics/skills](https://github.com/anthropics/skills) (Apache-2.0; theme-factory tem licença própria) | Interfaces com identidade, pôsteres em PNG/PDF, arte generativa, manual de marca (modelo) e temas de cor e fonte. | Cópia | Sites e artes sem cara genérica. |
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) (MIT) | Gera paleta, fontes e estilo pelo tipo de negócio. Precisa de Python 3. | Cópia | Site de pizzaria, salão ou loja. |
| web-asset-generator | [alonw0/web-asset-generator](https://github.com/alonw0/web-asset-generator) (MIT) | Favicons, ícones e imagens para redes sociais. | Cópia | Acabamento de site. |
| frontend-slides | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) (MIT) | Apresentações HTML animadas. | Cópia | Proposta para cliente e seminário. |

## Marketing e vendas

A maioria vem de [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT, 50 skills, em inglês e pensado para SaaS). Peça para adaptar ao negócio local e ao Brasil. Instalação: Cópia.

| Skill | Repositório | O que faz | Pra quem serve |
|---|---|---|---|
| copywriting, copy-editing | marketingskills | Escreve e revisa textos de página de venda. | Site e proposta. |
| social, content-strategy | marketingskills | Conteúdo e calendário para redes sociais. | Instagram de clientes. |
| offers, pricing | marketingskills | Monta a oferta, os pacotes e o preço. | Quem vende serviço. |
| prospecting, sales-enablement | marketingskills | Lista de clientes, roteiro de venda, objeções. | Prospecção. |
| sms | marketingskills | Fluxos de SMS e WhatsApp. | Atendimento. |
| seo-audit, schema, ai-seo | marketingskills | SEO no Google, dados estruturados e ser citado por IAs. | Aparecer nas buscas. |
| cro, lead-magnets, referrals | marketingskills | Conversão, iscas de contato e programa de indicação. | Cardápio e site que vendem mais. |
| competitor-profiling, customer-research, marketing-psychology | marketingskills | Concorrentes, pesquisa com cliente e psicologia de compra. | Entender o mercado. |
| lead-research-assistant, domain-name-brainstormer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) (Apache-2.0) | Qualifica leads; sugere domínios livres. | Prospecção e site novo. |
| hook-generator, content-matrix, gemini-carousel, reels-scripting, youtube-thumbnail | [charlie947/social-media-skills](https://github.com/charlie947/social-media-skills) (MIT) | Ganchos, ideias de post, carrosséis, roteiro de Reels e capa de vídeo. | Redes sociais. |
| humanizer | [blader/humanizer](https://github.com/blader/humanizer) (MIT) | Tira a cara de IA do texto (em inglês; aqui tem a versão em pt-BR: `humanizar-texto-pt`). | Legendas e trabalhos. |

## Documentos

| Skill | Repositório | O que faz | Instalar |
|---|---|---|---|
| docx, pdf, pptx, xlsx | [anthropics/skills](https://github.com/anthropics/skills) (source-available) | Word, PDF, PowerPoint e Excel de verdade. | Cópia |
| doc-coauthoring, internal-comms | [anthropics/skills](https://github.com/anthropics/skills) (Apache-2.0) | Escrever documentos em parceria; relatórios e comunicados. | Cópia |
| tailored-resume-generator, content-research-writer, invoice-organizer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) (Apache-2.0) | Currículo para uma vaga, texto com fontes, organizar notas fiscais. | Cópia |

## Automação

| Skill | Repositório | O que faz | Instalar |
|---|---|---|---|
| n8n (14 skills) | [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) (MIT; precisa do n8n-mcp) | Fluxos e agentes no n8n. | Cópia de `skills/*` |
| file-organizer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) (Apache-2.0) | Organiza pastas e acha arquivos duplicados. | Cópia |
| Skill_Seekers (ferramenta) | [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) (MIT) | Transforma documentação em skill. | `pip install skill-seekers` |

## Produtividade

| Skill | Repositório | O que faz | Instalar |
|---|---|---|---|
| obsidian-markdown, obsidian-bases, json-canvas, obsidian-cli, defuddle | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) (MIT) | Notas, bases, canvas e CLI do Obsidian; salvar páginas da web limpas. Feito pelo CEO do Obsidian. | Cópia |
| Notion Skills | [makenotion/claude-code-notion-plugin](https://github.com/makenotion/claude-code-notion-plugin) (licença não informada) | Plugin oficial do Notion com 4 skills e o conector. | `/plugin marketplace add makenotion/claude-code-notion-plugin` |
| handoff | [mattpocock/skills](https://github.com/mattpocock/skills) (MIT) | Resume a conversa para continuar em outra sessão. | npx `mattpocock/skills` |
| meeting-insights-analyzer | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) (Apache-2.0) | Padrões em transcrições de reunião. | Cópia |
| session-log | [michalparkola/tapestry-skills-for-claude-code](https://github.com/michalparkola/tapestry-skills-for-claude-code) (MIT) | Diário semanal do que você fez. | Cópia |

## Segurança

| Skill | Repositório | O que faz | Instalar |
|---|---|---|---|
| fp-check, sharp-edges, supply-chain-risk-auditor, insecure-defaults, static-analysis, differential-review | [trailofbits/skills](https://github.com/trailofbits/skills) (CC-BY-SA-4.0) | Falso positivo, código perigoso, dependências, configurações inseguras, CodeQL/Semgrep e revisão de mudanças. | Cópia |
| code-security, semgrep, llm-security | [semgrep/skills](https://github.com/semgrep/skills) | Código seguro (OWASP), Semgrep e segurança de apps com IA. | Cópia |

## Vídeo e imagem

| Skill | Repositório | O que faz | Instalar |
|---|---|---|---|
| remotion (best-practices, captions, render) | [remotion-dev/skills](https://github.com/remotion-dev/skills) | Vídeo com React, legendas e renderização. | Cópia |
| hyperframes | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) (Apache-2.0) | Vídeo MP4 feito com HTML. Precisa de Node 22+ e FFmpeg. | Cópia |
| image-enhancer, video-downloader | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) (Apache-2.0) | Melhora imagens; baixa vídeos (respeite os direitos autorais). | Cópia |
| slack-gif-creator | [anthropics/skills](https://github.com/anthropics/skills) (Apache-2.0) | GIFs animados. | Cópia |

## Jogos (Minecraft Java)

Nenhuma é oficial. Quase todas são para a 1.21.x: confira a versão do seu modpack.

| Skill | Repositório | O que faz | Instalar |
|---|---|---|---|
| minecraft-modding, -datapack, -commands-scripting, -resource-pack, -server-admin, -plugin-dev, -imagegen | [jahrome907/minecraft-agent-skills](https://github.com/jahrome907/minecraft-agent-skills) (MIT) | Mods (NeoForge/Fabric/Forge), datapacks, comandos, texturas, servidor, plugins e artes. | Cópia |
| fabric, minecraft-texture, minecraft-model, minecraft-orchestra, geckolib, veil | [hairyf/skills](https://github.com/hairyf/skills) (MIT) | Fabric com documentação atual, texturas, modelos, mods grandes, animações e shaders. | npx `hairyf/skills` |
| minecraft-mod-dev | [chouzz/minecraft-mod-dev](https://github.com/chouzz/minecraft-mod-dev) (licença não informada) | Mods integrados com JEI, AE2 e Create. | `/plugin marketplace add chouzz/minecraft-mod-dev` |

---

## Onde achar mais skills

- [skills.sh](https://skills.sh): ranking e catálogo da Vercel; instala com `npx skills add <dono>/<repo>`.
- [agentskills.io](https://agentskills.io): especificação oficial do formato (pasta com `SKILL.md`).
- [officialskills.sh](https://officialskills.sh): skills oficiais de empresas (Anthropic, Neon, Supabase, Remotion).
- [claudskills.com](https://claudskills.com): registro independente com milhares de skills.
- [claudemarketplaces.com](https://claudemarketplaces.com): plugins, skills e servidores MCP.
- [kursku/skills](https://github.com/kursku/skills): o maior acervo em português que achei (mais de 500 skills em PT). Sem licença declarada; navegue com cuidado.
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills), [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills), [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills), [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code): listas curadas.
- [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills): biblioteca com cerca de 2.600 skills (MIT).
- Guia oficial em português: [Agent Skills na documentação da Anthropic](https://platform.claude.com/docs/pt-BR/agents-and-tools/agent-skills/overview).

## Lacunas que este repositório preenche

A pesquisa achou necessidades sem skill boa em português. Por isso, este repositório criou:

| Lacuna | Skill daqui |
|---|---|
| Venda por WhatsApp para negócio local | [abordagem-whatsapp-vendas](skills/abordagem-whatsapp-vendas/README.md) |
| Cardápio digital com pedido pelo WhatsApp | [cardapio-digital](skills/cardapio-digital/README.md) |
| Legenda e calendário de Instagram em pt-BR | [legenda-instagram-negocio](skills/legenda-instagram-negocio/README.md) |
| Orçamento e proposta em reais | [orcamento-servicos](skills/orcamento-servicos/README.md) |
| Currículo de Jovem Aprendiz no padrão brasileiro | [curriculo-jovem-aprendiz](skills/curriculo-jovem-aprendiz/README.md) |
| Cronograma de estudos e revisão espaçada | [organizador-de-estudos](skills/organizador-de-estudos/README.md) |
| Tutor de SQL para iniciante | [tutor-sql](skills/tutor-sql/README.md) |
| Comparar preço em lojas brasileiras | [comparador-produtos-br](skills/comparador-produtos-br/README.md) |
| Assistente de voz em português | [assistente-voz-jarvis](skills/assistente-voz-jarvis/README.md) |
| LGPD, política de privacidade e termos | [legal-compliance](skills/legal-compliance/README.md) |

Falta alguma? [Sugira uma skill](../../issues/new?template=sugerir-skill.yml).
