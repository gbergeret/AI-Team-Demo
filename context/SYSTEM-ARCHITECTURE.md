# System architecture

The one map of how this team is wired — request flow, roles, gates, memory,
permissions, and the repo layout. Read this to onboard or audit; load the specifics
on demand from the files it points to.

## Request flow
```
User
  └─▶ CoS  (front door, runs in the main session)
        ├─ delegates a six-field brief ─▶ EA (executes)
        ├─ QA loop        (graded findings; only [BLOCK] gates; up to 3 rounds)
        └─ CISO gate      (after QA, only on permission / connector / config changes)
        ◀─ integrates ─ returns to you  (only a PASS or an escalation reaches you)
```

## Roles
Each role has `roles/<role>/ROLE.md` (mandate) **and** `.claude/agents/<role>.md`
(runtime manifest, except the CoS which runs in the main session) — both must agree
(see "Adding a role" in `CLAUDE.md`).

| Role | Job | Runs in | Reads/writes |
|---|---|---|---|
| CoS | front door / orchestrator | main session | this repo |
| EA | executes the CoS's briefs | subagent | this repo + granted connectors |
| QA | quality gate | subagent | read-only |
| CISO | security gate (after QA) | subagent | read-only |

## Gates (the order is invariant)
1. **QA** — always in the path for non-trivial work; grades findings, only `[BLOCK]`
   gates resubmission.
2. **CISO** — conditional, **after** QA, only when a change touches permissions,
   connectors, or configuration. Read-only: it flags, the producing role fixes.

A gate is never an entry point and always runs on QA-passed work.

## Memory
- **Shared** `MEMORY.md`; **role** `roles/<role>/MEMORY.md` — the more specific wins.
- Active work lives in `projects/` (a one-line pointer in `MEMORY.md`); context is
  loaded on demand via `context/INDEX.md`.

## Permissions
Deny-by-default, **action tiers** (READ/ANNOTATE/EDIT/CREATE/TRANSITION/DELETE, with
DELETE never granted), the **two-place model** (`PERMISSIONS.md` grant + the agent's
`tools:` allow-list, stricter wins), and the `.claude/settings.json` floor. The
constitution is `context/GOLDEN-RULES.md`.

## Repo layout
```
AI-Team-Demo/
├── CLAUDE.md            # startup routine, the team, gates, memory
├── MEMORY.md            # shared memory (one-line pointer per project)
├── PERMISSIONS.md       # action-tier grants matrix
├── projects/           # active work, one folder per project
├── context/            # GOLDEN-RULES, INDEX, PRINCIPLES, PROFILE, VOICE, SYSTEM-ARCHITECTURE
├── roles/<role>/       # ROLE.md + MEMORY.md per role (cos, ea, qa, ciso)
├── playbooks/          # welcome wizard + save/reload + daily summary
├── scripts/            # token-cost report
└── .claude/
    ├── agents/          # EA / QA / CISO manifests + _TEMPLATE.md (CoS is the main session)
    └── settings.json    # permissions floor
```
