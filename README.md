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
  `MEMORY.md` (what it has learned). Roles: `cos` (front door), `ea`, `qa`,
  `ciso` (security gate).

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
- **A security gate (the CISO)** (`roles/ciso/ROLE.md`) — a read-only **second
  gate** that runs *after* QA, on QA-validated work, and only when a change
  touches permissions, connectors, or configuration. It flags concerns; the
  producing role fixes them (back through QA), never the CISO.
- **Playbooks** — the welcome wizard and `save` / `reload` (trigger-word), plus a
  **scheduled** one: the daily summary, a read-only morning briefing from your
  Google Calendar, run by the EA.
- **Governance** — `context/GOLDEN-RULES.md` (the constitution, loaded first),
  `PERMISSIONS.md` (the action-tier grants matrix), and `context/PRINCIPLES.md`
  (how you like work done). A capability is real only when granted in both
  `PERMISSIONS.md` and the role's allow-list (the two-place model), with a
  `.claude/settings.json` floor denying what should never happen.
- **Git as the store** — versioned, diffable, revertable.

## Changing things: the governed flow (advanced)
Because everything here is plain Markdown in git, the most robust way to change
anything — memory, context, roles, or the rules themselves — is a real git flow:

1. **Branch** off `main`.
2. **Edit** the files.
3. **Open a pull request** and review it — the QA loop checks the change before it
   lands, the same way it gates any other deliverable.
4. **Merge** once it passes.
5. **Revert** to undo — `git revert` drops a bad change and keeps *both* the
   mistake and its correction in the history, so nothing is silently rewritten.

This is the apex of "git as the store": every change is proposed, reviewed, and
reversible, with a full audit trail. It is where review matters most — changes to
rules or permissions belong here. It is also an **advanced** workflow, so for
everyday use we hide it behind the `save` and `reload` playbooks
(`001-save-to-main`, `002-rebase-from-main`), which commit straight to `main` in
one step. The trade-off is deliberate: the playbooks are simple but have **no
review**; the governed flow adds the review gate and a clean history in exchange
for a little ceremony. Start with the playbooks; reach for the governed flow when
a change is worth reviewing before it lands.

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
