# 003 - Daily summary

**Cadence:** Daily (scheduled). Set this up as a recurring routine in Claude Code
so it runs each morning.

A short morning briefing of your day, built from Google Calendar. Read-only. The EA runs it (it holds the calendar read tools).

## Steps
1. Read today's events from Google Calendar (`list_events` for today; use
   `list_calendars` first if there is more than one calendar).
2. Summarise: how many meetings, the first and the last, and any back-to-back runs.
3. Flag what needs attention: a meeting with guests but no location or video link,
   or two events that overlap.
4. Keep it tight, a few lines, in your voice (`context/VOICE.md`).

## Output
Present the briefing in chat. Change nothing on the calendar, this is read-only
(calendar writes are denied).

## Done when
The briefing covers today's events and flags any location-less or clashing
meetings, or says the day is clear.
