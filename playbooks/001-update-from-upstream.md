# 001 - Update from upstream

**Cadence:** On-demand (say "update from upstream", or "check for updates").

Bring the latest improvements from the original demo this was copied from into your
own copy. The README's "How to start" copies the whole demo in once, as your setup;
this playbook is the *update* version of that copy - it checks the latest upstream and
copies the newer template files in, so you gain new features and fixes without losing
anything personal. (Sibling to "rebase from main", which syncs *your own* saved work
across devices; this one is about the *template's* changes, not yours.)

**Upstream:** `gbergeret/AI-Team-Demo` - the repo this demo was copied from. If you
copied from somewhere else, change this line to your source `owner/repo`.
**Last synced:** `not set` - the upstream commit this copy was last updated to. Stored
here alongside the upstream repo; the playbook uses it as the baseline and rewrites it
to the new upstream HEAD after each successful update, so next time it only looks at
what changed since. The welcome wizard sets it at copy time; if it is ever `not set`,
the first update establishes it from the file comparison.

## Tools & permissions
- **git** only (local). Reading the upstream is a plain, unauthenticated `git clone` of
  a public repo into a temporary folder *outside* this repo, so no connector or login is
  needed and your own repo's git history is never touched. No writes to any remote until
  the person confirms; nothing is ever deleted. (The optional PR path just uses a normal
  git push plus GitHub in the browser - the same "governed flow" the README describes.)

## Scope
- **In:** framework / scaffolding files - playbooks, `CLAUDE.md`, `README.md`,
  `PERMISSIONS.md`, `scripts/`, the `_TEMPLATE.md` files, `context/INDEX.md`, the role
  mandates (`roles/*/ROLE.md`), the subagent manifests (`.claude/agents/`), and the
  governance files (`context/GOLDEN-RULES.md`, `context/PRINCIPLES.md`).
- **Out (never auto-changed):** your personal content - `MEMORY.md`, each role's
  `roles/*/MEMORY.md`, `context/PROFILE.md`, `context/VOICE.md`, and everything under
  `projects/`. These are yours: the playbook shows you if they differ from upstream, but
  never overwrites them unless you say so for that specific file.

## Steps
1. **Find the upstream and baseline.** Use the `owner/repo` and the **Last synced**
   commit on the lines above. If `owner/repo` is wrong, ask the person for the right one.
2. **Clone the latest upstream.** Clone it into a temporary folder *outside* this repo,
   full history included, so your own repo is never touched:
   `tmp="$(mktemp -d)"; git clone https://github.com/gbergeret/AI-Team-Demo "$tmp"`.
   Read from `$tmp`, compare against your repo, and delete `$tmp` when done (step 6). A
   clone - not a remote - keeps the two repos cleanly separate (they share no history,
   and nothing from upstream lands in your repo's `.git`).
3. **Understand what changed - history and files together.** The commit log is the
   *starting point*, not the whole answer; understanding is the combination of the two.
   - **History (what and why):** in the clone, if **Last synced** is set,
     `git -C "$tmp" log <last-synced>..HEAD` is exactly what changed since; if it is
     `not set`, read the recent log (`git -C "$tmp" log --oneline`) and reason about what
     post-dates the copy. Use `git -C "$tmp" show <sha>` for the reasoning behind a change.
   - **Files (what is really there now):** correlate each change against the actual files
     by comparing the clone with your repo -
     `git diff --no-index <path> "$tmp"/<path>` shows what adopting upstream's version
     would change. A commit may be superseded by a later one, already present locally, or
     overlap something you edited; only the file comparison shows the true current state.
   Combine both into a short, accurate changelog: "since your copy, upstream added X,
   improved Y, fixed Z", each mapped to the files it touches.
4. **Copy the updates in - framework files only.** Copy the newer framework / scaffolding
   files from the clone into this repo (`cp "$tmp"/<path> <path>`): the same "copy from
   upstream" the README setup does, but incremental - only what changed, and never over
   your personal files (`MEMORY.md`, `roles/*/MEMORY.md`, `context/PROFILE.md`,
   `context/VOICE.md`, `projects/`). If you *also* changed a framework file locally, flag
   it and let the person decide what wins. Never delete a file that exists locally but not
   upstream - it may be their own.
5. **Show the plan and confirm.** Present the changelog (grouped, with the why) and the
   exact list of files that would be copied in, plus anything held back (personal files,
   local edits). Nothing is applied until the person says go.
6. **Apply as one clean commit, and record the sync.** On confirmation: copy the chosen
   updates in and re-stamp **Last synced** (*after* the copy - this playbook is itself a
   framework file, so it must be stamped last). Commit the whole update as a **single
   clean commit** - every copied framework file plus the `Last synced` bump together -
   with a clear message such as `Update from upstream: <one-line changelog>`; never split
   it across several commits. Advance **Last synced** to the clone's HEAD
   (`git -C "$tmp" rev-parse HEAD`) only if you brought in *everything*; if the person
   skipped or cherry-picked, hold the baseline so the skipped changes resurface next run.
   Then delete the temporary clone (`rm -rf "$tmp"`) and back it up: push that commit to
   `main` (quick), or open a pull request from it (reviewed) - the person's choice.

## Rules
- History is the starting point, not the whole story: read the upstream log for *what*
  and *why*, then correlate every change against the actual files before copying.
  Understanding is the combination, not the log alone.
- Update **Last synced** on every run that applies changes - advance it to the clone's
  HEAD only when the copy is fully in sync, never past a change the person skipped. The
  pointer must never claim a sync that did not happen.
- Read-only until the person confirms both the apply set and the path.
- Never touch a personal file (`MEMORY.md`, `roles/*/MEMORY.md`, `context/PROFILE.md`,
  `context/VOICE.md`, `projects/`) without an explicit yes for that specific file.
- Never delete. A file that exists locally but not upstream is left in place and
  flagged, not removed - it may be the person's own addition.
- Read the upstream from a throwaway clone *outside* this repo, never by adding it as a
  remote - keep the two histories separate - and delete the clone (`rm -rf "$tmp"`) when
  done. Never force anything onto a remote.
- If the upstream can't be reached or looks wrong, ask - don't guess.

## Output / End-of-run report
- A short summary: upstream `owner/repo`, the baseline it compared from, the changelog
  it found, what was offered, which path was chosen, what was applied, what was left
  untouched (the personal files), and the new **Last synced** commit.

## Done when
- The chosen framework updates are in the copy as one clean commit (pushed to `main`, or
  on a branch with an open pull request), the personal files are untouched, nothing was
  deleted, **Last synced** points at the commit just synced, and the change is saved (or
  the PR is open).
