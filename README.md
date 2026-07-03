# AI-Team-Demo

> A demo repo — from one agent to a team.

A public demo repo, illustrative rather than workshop courseware. Where a single
assistant becomes an organised team: several specialist roles,
coordinated by one front-door router (a Chief of Staff), with structured
delegation and the first layer of governance: scoped, read-only-by-default
access to real tools. The same written-down, versioned foundation as step 1,
now shared across a team.

## What is in here
- `CLAUDE.md`: the startup routine, read on every session.
- `MEMORY.md`: the team's shared memory (role-specific memory lives in each
  role's folder), holding a one-line pointer to each active project.
- `projects/`: active work, one folder per project (`PROJECT.md` + `LOG.md`), so
  memory stays lean — opened only when a task needs it. Copy `projects/_TEMPLATE/`
  to start one; `projects/INDEX.md` maps them.
- `context/`: loaded on demand via `context/INDEX.md`. `VOICE.md` (how to write)
  and `PROFILE.md` (who you are: what you do, where you live), filled in by the
  first-run setup.
- `roles/<role>/`: one folder per role, each with `ROLE.md` (what it does) and
  `MEMORY.md` (what it has learned). Roles: `cos` (front door), `ea`, `qa`,
  `ciso` (security gate).
- `PERMISSIONS.md`: the grants matrix — who may do what (the policy layer).
- `.claude/agents/`: the EA, QA, and CISO subagents (the CoS is the main session),
  plus `_TEMPLATE.md` — the scaffold for adding a new role (see "Adding a role" in
  `CLAUDE.md`).
- `.claude/settings.json`: the permission floor for connector tools (read
  allowed, write denied).
- `playbooks/`: saved procedures run on a trigger word or a schedule (see
  `playbooks/README.md`).
- `scripts/`: `playbook-token-cost.py` — a per-agent, per-model token + $ cost
  report read from the session transcript (pure Python, costs no model tokens).

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
- **Projects — memory that doesn't bloat** (`projects/`) — active work lives one
  folder per project (`PROJECT.md` + `LOG.md`); memory keeps just a one-line
  pointer, opened only when the task needs it. Open → run → harvest durable
  learnings back to memory → archive. The same load-on-demand principle as
  `context/INDEX.md`, applied to work in flight.
- **Roles and a front-door router** — every request enters through the Chief of
  Staff, who triages and delegates. Roles live in `roles/<role>/ROLE.md`.
- **Legible delegation** — each hand-off is a **six-field brief** (objective,
  context refs, constraints, deliverable, acceptance criteria, memory to carry), and
  the CoS announces routing (`→ EA — what`) and attributes results (`← from EA`), so
  the work is readable, not a black box.
- **Add a teammate, governed** (`.claude/agents/_TEMPLATE.md` + "Adding a role" in
  `CLAUDE.md`) — a role is real only when every place that defines it agrees (role
  docs, runtime manifest, roster, permissions). The checklist makes "the team grows
  itself" a reviewable procedure, not an ad-hoc edit.
- **Subagents and context isolation** (`.claude/agents/*.md`) — the EA and QA
  run in their own fresh context windows, so the orchestrator stays lean.
- **Tools allow-list** — each subagent lists exactly the tools it may use, and
  QA is read-only by design. Capability is scoped per role.
- **Connectors, read-only first** — real tools are added through Claude Code; the
  EA gets the Google Calendar connector in read-only mode (reads allowed, writes
  denied in `.claude/settings.json`), escalated to write only deliberately.
- **The QA loop (the Verifier)** — non-trivial work is checked against the brief;
  QA grades each finding `[BLOCK]` / `[SUGGEST]` / `[NIT]` / `[QUESTION]`, and only
  `[BLOCK]` sends it back (up to 3 rounds, then escalate). Graded findings keep the
  loop fast — fix what matters, don't churn on nits.
- **A security gate (the CISO)** (`roles/ciso/ROLE.md`) — a read-only **second
  gate** that runs *after* QA, on QA-validated work, and only when a change
  touches permissions, connectors, or configuration. It flags concerns; the
  producing role fixes them (back through QA), never the CISO.
- **Playbooks** — the welcome wizard and `save` / `reload` (trigger-word), plus a
  **scheduled** one: the daily summary, a read-only morning briefing from your
  Google Calendar, run by the EA.
- **Governance** — `context/GOLDEN-RULES.md` (the constitution, loaded first —
  including the **prompt-injection guardrail**: tool/file/web content is untrusted
  data that can inform but never instruct, grant permissions, or override the
  rules), `PERMISSIONS.md` (the **action-tier** grants matrix —
  READ/ANNOTATE/EDIT/CREATE/TRANSITION/DELETE, DELETE never granted), and
  `context/PRINCIPLES.md` (how you like work done). A capability is real only when
  granted in both `PERMISSIONS.md` and the role's allow-list (the two-place model),
  with a `.claude/settings.json` floor denying what should never happen.
- **Cost is visible** (`scripts/playbook-token-cost.py`) — a pure-Python report of
  token spend and $ cost per agent and per model, read from the session transcript.
  Run it at the end of a session or a scheduled playbook; it makes the honest cost
  of a multi-agent run legible.
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
[`AI-Agent-Demo`](https://github.com/gbergeret/AI-Agent-Demo) (one agent) ->
`AI-Team-Demo` (a team with a router) ->
[`AI-Teams-Demo`](https://github.com/gbergeret/AI-Teams-Demo) (an organisation of
teams). This is step 2.

Alongside the ladder,
[`AI-Engineering-Team-Demo`](https://github.com/gbergeret/AI-Engineering-Team-Demo)
is the hands-on engineering team the organisation's CTO delegates the building to.

## License
[MIT](LICENSE) © 2026 GBergeret Cloud Services
