# 000 - Welcome wizard

A short, friendly first-run interview. The goal: learn the basics about who you
are and how you want to be spoken to, then save them so the team remembers from
now on. It runs once: when it finishes, it saves your answers and cleans up after
itself (removing the wizard and its first-run hook), then lets you choose how to save
the changes.

## When to run
On the first session, if `context/PROFILE.md` still shows the placeholder name
("(not set yet)"). Once onboarding is done, this file is gone and it never runs
again.

## How to run
Ask one question at a time. Keep it warm and brief, and accept whatever the
person gives (there are no wrong answers). They can skip any question. When you
are done, write the answers to the files and show what you saved.

### Questions (keep it to these, do not add more)
1. **What should I call you?**
   Save to `context/PROFILE.md` (Name).
2. **How do you like to be spoken to?** (for example: direct, warm, formal,
   concise, a mix)
   Save to `context/VOICE.md`.
3. **What do you do?** One line about your work or field.
   Save to `context/PROFILE.md` (What you do).
4. **Where do you live?**
   Save to `context/PROFILE.md` (Where you live).
5. **What language should I reply in?**
   Save to `context/PROFILE.md` (Language).

## After the interview
- Write each answer into the right place in `context/PROFILE.md` and
  `context/VOICE.md`, replacing the placeholders. Keep it tidy.
- **Offer to open a first project.** Ask if there's something in flight; if so, copy
  `projects/_TEMPLATE/` to `projects/<today>-<slug>/` (today as `YYYY-MM-DD`), fill in
  its objective and owner, and add a one-line pointer under `## Projects` in
  `MEMORY.md`. It shows the projects layer working from minute one and keeps memory
  lean. If there's nothing yet, skip it.
- **Make the repo theirs.** Update `README.md` so it reads as this person's own
  private team, not a public demo:
  - Reframe the top (title, tagline, and intro paragraph) to name whose team it now is
    (use the name from question 1, for example "Marie's private team") and note it was
    set up from the public demo.
  - Remove the sections that only make sense for the public demo or a first-time
    setup: "How to start" (they have already started) and "The progression" (the demo
    ladder to the other repos).
  - Keep the rest as the owner's reference: "What is in here", "Concepts in this
    repo", the governed-flow section, and the Codex-equivalents note.
- Delete this playbook (`playbooks/000-welcome-wizard.md`): one-time setup, not
  needed once it has run.
- Clean up `CLAUDE.md`: remove the "## First run: the welcome wizard" section, so
  nothing points at the deleted playbook.
- Commit all of these changes together in a single commit (the filled-in profile, the
  voice, the personalised `README.md`, the removed wizard, and the cleaned-up
  `CLAUDE.md`). That commit is the record of your onboarding. Then hand the choice of
  how to save it to the user, rather than opening a pull request automatically.
- Close with exactly this: "You're all set now. If you're comfortable with Git, you
  can raise a PR to merge into main. If you're a beginner, just ask me to save changes
  and I'll run the save-to-main playbook."
