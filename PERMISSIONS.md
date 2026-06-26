# PERMISSIONS.md

The policy layer: who may do what, with which tool. **Deny-by-default** —
anything not listed here stays read-only. A capability is real only when it is
granted here **and** listed in the role's `.claude/agents/<role>.md` allow-list.
Both must agree; the stricter wins. **DELETE is never granted.**

## Action tiers
| Tier | Means |
|---|---|
| READ | view, search, fetch |
| ANNOTATE | add or edit comments / notes |
| EDIT | change existing items |
| CREATE | make new items |
| TRANSITION | change state (complete, archive, move) |
| DELETE | remove permanently — never granted |

## Grants
| Role | Surface | Granted |
|---|---|---|
| CoS | this repo's files | READ, EDIT, CREATE |
| EA | this repo's files | READ, EDIT, CREATE |
| EA | external connectors (e.g. calendar) | READ |
| QA | everything | READ only |
| CISO | everything | READ only |

Anything not listed stays READ-only. Connectors start read-only; grant a scoped
write both here and in the role's allow-list, deliberately, when you need it.
