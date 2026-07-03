# NNN - <Playbook name>

**Cadence:** On-demand (say "<trigger>") — *or* — Scheduled (e.g. daily; set it up
as a recurring routine in Claude Code). Pick one and delete the other.

<One line: what this playbook is for and who runs it.>

## Tools & permissions
- <which tools / connectors it uses, at what tier — read-only unless a write is
  explicitly granted in `PERMISSIONS.md` and the role's allow-list>.

## Scope
- **In:** <what it covers>.
- **Out:** <what it deliberately does not touch>.

## Steps
1. <step>
2. <step>

## Rules
- <constraints — e.g. read-only, never send, ask before acting if unsure>.

## Output / End-of-run report
- <what it produces, and where it goes>.
- If it ran subagents or on a schedule, end with `scripts/playbook-token-cost.py`
  and paste the per-agent, per-model token + $ table.

## Done when
- <the definition of done — the check that says this run is complete>.
