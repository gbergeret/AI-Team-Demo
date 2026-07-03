---
# Copy this file to .claude/agents/<role>.md to add a role, then fill it in and
# follow "## Adding a role" in CLAUDE.md. Delete these comments in the real file.
name: <role>            # kebab-case; matches roles/<role>/ and how you delegate to it
description: <one line — what this role is for and when to use it. This is the routing trigger, so make it specific.>
tools: Read, Write, Edit, Glob, Grep   # least privilege: list only what it needs, no wildcards. A read-only gate (QA/CISO) is `Read, Glob, Grep`.
model: sonnet           # opus for heavy judgement, sonnet for routine, haiku for light
effort: medium          # low | medium | high | xhigh | max — set by the role's HARDEST actual task, not its title
---
You are the <Role> on the team.

Your full mandate is in `roles/<role>/ROLE.md`. In short:
- <what it takes in, and what it produces>
- <who it works with>
- Return the result to the CoS, not straight to the user.

<!--
Adding a role is a checklist, not just this file — see "## Adding a role" in CLAUDE.md.
In short: create roles/<role>/{ROLE.md,MEMORY.md} + this manifest, add the role to the
roster in CLAUDE.md and README.md, grant its surface in PERMISSIONS.md (two-place model),
then open a PR. A role is only "real" when all of those agree.
-->
