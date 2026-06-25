# CLAUDE.md

The startup routine. Read this first, on every session.

## Load on every session
1. `MEMORY.md`: what the team has learned and the work in flight.
2. `context/VOICE.md`: how I want you to write and talk to me.

## The team
This is not one agent, it is a small team. Three roles:
- **Chief of Staff (CoS)**: the front door. Every request comes to CoS, who
  handles it or routes it. See `roles/cos.md`.
- **Executive Assistant (EA)**: executes the work CoS hands off. `roles/ea.md`.
- **QA**: checks a deliverable before it reaches me. `roles/qa.md`.

Load the role you are acting as before you start.

## How work flows
CoS reads the request, decides do-it or delegate, and hands execution to the EA.
For anything non-trivial CoS runs the QA loop: QA checks the work against the
brief; if QA returns defects, it goes back to the EA to revise and QA checks
again, up to 3 rounds. If it still has not passed after 3 rounds, CoS stops and
escalates to me with the gap. Only a PASS (or that escalation) reaches me.

## Keep memory current
Update `MEMORY.md` in place when you learn something. Replace what is outdated.
