# ai-team-base

> Workshop 2: from one agent to a team.

Where a single assistant becomes an organised team. Several specialist roles,
coordinated by one front-door router (a Chief of Staff), with structured
delegation and the first layer of governance: scoped, read-only-by-default
access to real tools. The same written-down, versioned foundation as step 1,
now shared across a team.

## What is in here
- `CLAUDE.md`: the startup routine, read on every session.
- `MEMORY.md`: the team's shared memory (role-specific memory lives in each
  role's folder).
- `context/`: loaded on demand via `context/INDEX.md`. `VOICE.md` (how to write)
  and `PROFILE.md` (who you are: what you do, where you live), filled in by the
  first-run setup.
- `roles/<role>/`: one folder per role, each with `ROLE.md` (what it does) and
  `MEMORY.md` (what it has learned). Roles: `cos` (front door), `ea`, `qa`.

## How to start
1. Fork or clone this repo.
2. Open it in Claude Code.
3. Say **"Hi"** to kick off. On the first run that triggers a quick setup (the
   welcome wizard); after that the Chief of Staff triages each request, hands
   work to the EA, and runs anything non-trivial past QA before it reaches you.

## Concepts in this repo
- **Written memory and context** (`MEMORY.md`, `context/` via `INDEX.md`) —
  loaded on demand; identity in `PROFILE.md`, tone in `VOICE.md`.
- **Layered memory** — a shared team `MEMORY.md` plus a per-role
  `roles/<role>/MEMORY.md`; the more specific layer wins.
- **Roles and a front-door router** — every request enters through the Chief of
  Staff, who triages and delegates. Roles live in `roles/<role>/ROLE.md`.
- **Subagents and context isolation** (`.claude/agents/*.md`) — the EA and QA
  run in their own fresh context windows, so the orchestrator stays lean.
- **Tools allow-list** — each subagent lists exactly the tools it may use, and
  QA is read-only by design. Capability is scoped per role.
- **The QA loop (the Verifier)** — non-trivial work is checked against the brief;
  on defects it goes back to the EA, up to 3 rounds, then escalates.
- **Playbooks** — the welcome wizard, plus `save` and `reload`.
- **Governance** — `context/GOLDEN-RULES.md` (the constitution, loaded first),
  `PERMISSIONS.md` (the action-tier grants matrix), and `context/PRINCIPLES.md`
  (how you like work done). A capability is real only when granted in both
  `PERMISSIONS.md` and the role's allow-list (the two-place model), with a
  `.claude/settings.json` floor denying what should never happen.
- **Git as the store** — versioned, diffable, revertable.

## Claude Code files (and Codex equivalents)
Most of this repo is plain Markdown that copies to any agent runner unchanged:
`MEMORY.md`, `context/`, the `roles/<role>/` docs, and `playbooks/` (playbooks are
just SOPs written down, not the Claude "skills" feature). Only a few things are
genuinely Claude Code-specific:

| This repo (Claude Code) | Codex equivalent |
|---|---|
| `CLAUDE.md` (auto-loaded startup file) | `AGENTS.md` |
| `.claude/agents/*.md` (named subagents) | `.codex/agents/*.toml` (custom agents; not auto-delegated, you delegate explicitly) |
| the `tools:` allow-list in a subagent | `approval_policy` + `sandbox_mode` in `config.toml` (an approval/sandbox model, not a literal tool allow-list) |

## The progression
[`ai-agent-base`](https://github.com/gbergeret/ai-agent-base) (one agent) ->
`ai-team-base` (a team with a router) ->
[`ai-teams-base`](https://github.com/gbergeret/ai-teams-base) (an organisation of
teams). This is step 2.
