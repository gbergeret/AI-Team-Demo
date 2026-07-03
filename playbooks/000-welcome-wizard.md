# 000 - Welcome wizard

A short, friendly first-run interview. The goal: learn the basics about who you
are and how you want to be spoken to, then save them so the team remembers from
now on. It runs once: when it finishes, it saves your answers and cleans up after
itself (removing the wizard and its first-run hook) in a single pull request.

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
- Delete this playbook (`playbooks/000-welcome-wizard.md`): one-time setup, not
  needed once it has run.
- Clean up `CLAUDE.md`: remove the "## First run: the welcome wizard" section, so
  nothing points at the deleted playbook.
- Open a pull request with all of these changes together (the filled-in profile,
  the voice, the removed wizard, and the cleaned-up `CLAUDE.md`). The PR is the
  record of your onboarding.
- Confirm in one line: "I have opened a PR with your details and removed the
  setup wizard. Review and merge it and you are set. You can change any of this
  any time."
