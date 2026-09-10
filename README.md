# Formations IA — Cursor & Claude Code

Série de vidéos en français sur les meilleures pratiques du codage assisté par IA avec **Cursor IDE** et **Claude Code**.

Chaque capsule comprend un script de tournage (`PLAN-VIDEO.md`) et une présentation interactive (site statique HTML/CSS/JS) affichée à l'écran pendant le tournage.

## Programme

| # | Capsule | Durée | Concept |
|---|---------|-------|---------|
| 1 | [**Rules**](rules/presentation/index.html) | ~10 min | `.cursor/rules/`, `.claude/rules/`, `CLAUDE.md`, `AGENTS.md`, format `.mdc`, migration depuis un `CLAUDE.md` monolithique |
| 2 | [**Commands & Skills**](commands_n_skills/presentation/index.html) | ~10 min | `/commands`, `SKILL.md`, Agent Skills standard (agentskills.io), Custom Modes, approche skills-first |
| 3 | [**Hooks**](hooks/presentation/index.html) | ~15 min | Intercepteurs déterministes, événements Pre/Post, 4 types (Command, Prompt, HTTP, Agent), compatibilité cross-Cursor/Claude |
| 4 | [**Spec-Driven AI Coding**](spec_driven/presentation/index.html) | ~20 min | Méthodologie SDD, pyramide de spécifications (Projet/Module/Fonctionnalité), notation EARS, workflow en 4 phases |
| 5 | [**MCP (Model Context Protocol)**](mcp/presentation/index.html) | ~18 min | Protocole ouvert, JSON-RPC, resources/tools/prompts, transport stdio vs HTTP, modèle de sécurité |
| 6 | [**Sub-agents**](subagents/presentation/index.html) | ~16 min | Isolation de contexte, parallélisme, spécialisation, agents intégrés (Explore, Bash, Browser), agents personnalisés |
| 7 | [**Choosing a Model**](model_arena/presentation/index.html) | ~13 min | Comparaison tarifaire OpenAI vs Anthropic, critères coût/vitesse/qualité/fiabilité, matrice tâche-modèle |
| 8 | [**Les SPECS au quotidien**](specs_workflow/presentation/index.html) | ~30 min | En quoi une spec aide à chaque étape (planification, coding, tests, reviews), décisions tracées, tests par cas, exemple fil rouge d'une connexion |

## Structure du projet

```
Formations/
├── index.html                     # Page d'accueil listant toutes les capsules
├── serve.py                       # Serveur local (Python)
├── rules/                         # Capsule 1
│   ├── PLAN-VIDEO.md
│   ├── presentation/              # Site statique (index.html, styles.css, script.js)
│   └── demo-project/              # Projet démo (fichiers de configuration IA)
├── commands_n_skills/             # Capsule 2
├── hooks/                         # Capsule 3
├── spec_driven/                   # Capsule 4
├── mcp/                           # Capsule 5
├── subagents/                     # Capsule 6
├── model_arena/                   # Capsule 7
└── specs_workflow/                # Capsule 8
```

Chaque dossier de capsule contient :

- **`PLAN-VIDEO.md`** — Script de tournage avec segments, timing et notes de réalisation
- **`presentation/`** — Site statique autonome utilisé comme diapositives (HTML + CSS + JS pur)

## Tech stack

- **HTML5 / CSS3 / Vanilla JavaScript** — aucun framework, aucun build step
- **Google Fonts** — Inter (corps) + JetBrains Mono (code)

## Utilisation locale

Ouvrez `index.html` directement dans un navigateur. Aucune dépendance, aucun serveur requis.

Toutes les capsules sont accessibles via des liens relatifs depuis la page d'accueil.

## Auteur

**David Thibault** — [TLMgo](https://github.com/TLMgo)
