# Projects

Active work lives here — one folder per project — so `MEMORY.md` stays lean. Memory
keeps a one-line pointer; the project folder holds the detail, opened only when a
task needs it. (This is the "P" of PARA: Projects.)

## Layout
- `projects/<YYYY-MM-DD-slug>/PROJECT.md` — the single source of truth: objective,
  owner, current state, decisions, refs.
- `projects/<YYYY-MM-DD-slug>/LOG.md` — a chronological digest of work and inputs.
- `projects/<YYYY-MM-DD-slug>/sources/` — digested raw input (optional).
- `projects/_TEMPLATE/` — copy this to start a project.
- `projects/INDEX.md` — the map of active and archived projects.

## Lifecycle
**Open → run → harvest → archive.** When a project closes, promote its durable
learnings to the right home (a line in `MEMORY.md`, or a role's memory), then move
the folder under `projects/_archive/`. Nothing lasting is lost; nothing transient
bloats memory.

## Why
Memory that doesn't bloat. The team reads a one-line pointer in `MEMORY.md` and
opens a project folder only when the task calls for it — written down, lean, loaded
on demand. It's the same principle as `context/INDEX.md`, applied to work in flight.
