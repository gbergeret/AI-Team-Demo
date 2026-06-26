# Playbooks

A playbook is a saved procedure the team can run: a short Markdown file with a
clear goal and steps. Keep them readable.

## Naming
Numbered for a stable order: `NNN-short-name.md`. `000` is reserved for
first-run setup.

## How they run
- **On demand:** you ask for it by name, or by its friendly verb (for example
  "save to main" or "rebase from main").
- **Scheduled:** some run on a cadence (e.g. daily); set them up as a recurring
  routine in Claude Code. See each playbook's **Cadence** line.
- **One-time:** some playbooks run once and then delete themselves (see `000`).

## Playbooks here
- `000-welcome-wizard.md`: first-run onboarding. Runs once, then deletes itself.
- `001-save-to-main.md`: save your work to the cloud (say "save to main").
- `002-rebase-from-main.md`: update to the latest saved work (say "rebase from main").
- `003-daily-summary.md`: a morning briefing from your calendar (scheduled, read-only).
