# ai-team-base

> Workshop 2: from one agent to a team.

Where a single assistant becomes an organised team. Several specialist roles,
coordinated by one front-door router (a Chief of Staff), with structured
delegation and the first layer of governance: scoped, read-only-by-default
access to real tools. The same written-down, versioned foundation as step 1,
now shared across a team.

## What is in here
- `CLAUDE.md`: the startup routine, read on every session.
- `MEMORY.md`: what the team has learned about you, updated in place as it goes.
- `context/VOICE.md`: how you want it to write and talk to you.
- `roles/`: one file per role. `cos.md` (the front door that routes),
  `ea.md` (executes the work), `qa.md` (checks it before it reaches you).

## How to start
1. Fork or clone this repo.
2. Open it in Claude Code.
3. Talk to it. It reads `CLAUDE.md` first, then your memory and voice. The
   Chief of Staff triages each request, hands work to the EA, and runs anything
   non-trivial past QA before it reaches you.

## The progression
[`ai-agent-base`](https://github.com/gbergeret/ai-agent-base) (one agent) ->
`ai-team-base` (a team with a router) ->
[`ai-teams-base`](https://github.com/gbergeret/ai-teams-base) (an organisation of
teams). This is step 2.
