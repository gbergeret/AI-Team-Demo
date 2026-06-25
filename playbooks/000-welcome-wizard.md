# 000 - Welcome wizard

A short, friendly first-run interview. The goal: learn the basics about who you
are and how you want to be spoken to, then save them so the team remembers from
now on. It runs once: when it finishes, it saves your answers and cleans up after
itself (removing the wizard and its first-run hook) in a single pull request.

## When to run
On the first session, if `MEMORY.md` still shows the placeholder name under
"About you". Once onboarding is done, this file is gone and it never runs again.

## How to run
Ask one question at a time. Keep it warm and brief, and accept whatever the
person gives (there are no wrong answers). They can skip any question. When you
are done, write the answers to the files and show what you saved.

### Questions (keep it to these, do not add more)
1. **What should I call you?**
   Save to `MEMORY.md`, under "About you".
2. **How do you like to be spoken to?** (for example: direct, warm, formal,
   concise, a mix)
   Save to `context/VOICE.md`.
3. **What do you do?** One line about your work or field.
   Save to `MEMORY.md`, under "About you".
4. **What language should I reply in?**
   Save to `MEMORY.md`, under "About you".

## After the interview
- Write each answer into the right section of `MEMORY.md` and `context/VOICE.md`,
  replacing the placeholders. Keep it tidy and well organised.
- Delete this playbook (`playbooks/000-welcome-wizard.md`): one-time setup, not
  needed once it has run.
- Clean up `CLAUDE.md`: remove the "## First run: the welcome wizard" section, so
  nothing points at the deleted playbook.
- Open a pull request with all of these changes together (the filled-in memory,
  the removed wizard, and the cleaned-up `CLAUDE.md`). The PR is the record of
  your onboarding.
- Confirm in one line: "I have opened a PR with your details and removed the
  setup wizard. Review and merge it and you are set. You can change any of this
  any time."
