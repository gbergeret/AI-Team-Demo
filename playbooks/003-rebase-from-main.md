# 003 - Rebase from main

Bring this device up to date with the latest saved work on `main`. The companion
to "save to main". Run it when the person says "rebase from main" (or "reload"),
for example when they switch from phone to laptop.

## What it does
Fetches the latest `main` from GitHub and replays any local changes on top, so
this device matches the saved version with a clean, linear history.

## Steps
1. Fetch the latest `main`.
2. Rebase the local work onto it (pull with rebase). If there are no local
   changes, this simply fast-forwards to the latest.

## After
Confirm in one line: "Rebased from main. You are on the latest saved version."
If nothing had changed, say so plainly.
