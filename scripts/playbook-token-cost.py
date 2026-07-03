#!/usr/bin/env python3
"""Summarise the token spend and $ cost of the current Claude Code session.

Reads the session transcript JSONL (the per-turn token usage Claude Code writes
for free) plus every subagent transcript under `<session>/subagents/`, and prints
a compact report broken down per agent and per model. The arithmetic happens here,
in plain Python — it costs no model tokens, so a playbook can call this as its
final step and paste the output into its End-of-run Report.

Usage:
  python3 scripts/playbook-token-cost.py                 # newest transcript for this repo
  python3 scripts/playbook-token-cost.py --transcript X  # an explicit .jsonl path
  python3 scripts/playbook-token-cost.py --json          # machine-readable output

Notes:
  - "main" is the orchestrator session (here, the CoS); each subagent
    (EA / QA / CISO) has its own transcript, listed separately.
  - The count excludes the final reporting turn(s) that come after this script
    runs — those tokens aren't in the transcript yet. The undercount is small.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys

# Per-million-token USD pricing. Cache write = 1.25x input (5-minute TTL) or 2x
# input (1-hour TTL); cache read = 0.1x input. Update these if pricing changes.
PRICING = {  # model family -> (input, output) per MTok
    "fable":  (10.0, 50.0),
    "opus":   (5.0, 25.0),
    "sonnet": (3.0, 15.0),
    "haiku":  (1.0, 5.0),
}
CACHE_WRITE_5M = 1.25
CACHE_WRITE_1H = 2.0
CACHE_READ = 0.1

# Friendly display names for the team's roles (the subagent slugs in .claude/agents/).
# Unknown agent types (e.g. explore) fall back to their slug.
ROLE_NAMES = {
    "main": "CoS (main)",
    "ea": "Executive Assistant",
    "qa": "QA",
    "ciso": "CISO",
}


def display_name(agent_type: str) -> str:
    return ROLE_NAMES.get(agent_type, agent_type)


def family_for(model: str) -> str | None:
    m = (model or "").lower()
    for fam in PRICING:
        if fam in m:
            return fam
    return None


def default_transcript() -> str | None:
    """Newest top-level .jsonl under the project dir for this cwd.

    Subagent transcripts live in a `<session>/subagents/` subdirectory, so the
    glob is deliberately non-recursive to pick the orchestrator session file.
    """
    slug = os.getcwd().replace("/", "-")
    base = os.path.expanduser(f"~/.claude/projects/{slug}")
    files = glob.glob(os.path.join(base, "*.jsonl"))
    if not files:
        files = glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl"))
    return max(files, key=os.path.getmtime) if files else None


def aggregate_usage(path: str) -> tuple[dict, set]:
    """Sum usage per exact model id from one transcript JSONL.

    Claude Code logs each assistant message multiple times (streaming /
    checkpoint rewrites carry the same message id), so usage is deduped by
    message id (one billed API response = one id) before summing. This matches
    the built-in `/usage` figures; summing every record double-counts ~2x.
    """
    latest: dict = {}  # dedupe key -> (model, usage); last write wins
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = obj.get("message") if isinstance(obj, dict) else None
            if not isinstance(msg, dict):
                continue
            usage = msg.get("usage")
            if not isinstance(usage, dict):
                continue
            key = msg.get("id") or obj.get("uuid") or len(latest)
            latest[key] = (msg.get("model", ""), usage)

    by_model: dict = {}
    unknown: set = set()
    for model, usage in latest.values():
        fam = family_for(model)
        if fam is None:
            if model:
                unknown.add(model)
            continue
        cc = usage.get("cache_creation") or {}
        row = by_model.setdefault(
            model,
            {"model": model, "family": fam, "input": 0, "output": 0,
             "cache_5m": 0, "cache_1h": 0, "cache_read": 0, "turns": 0},
        )
        row["turns"] += 1
        row["input"] += usage.get("input_tokens", 0) or 0
        row["output"] += usage.get("output_tokens", 0) or 0
        row["cache_read"] += usage.get("cache_read_input_tokens", 0) or 0
        row["cache_5m"] += cc.get("ephemeral_5m_input_tokens", 0) or 0
        row["cache_1h"] += cc.get("ephemeral_1h_input_tokens", 0) or 0
    return by_model, unknown


def tokens_in(row: dict) -> int:
    return row["input"] + row["output"] + row["cache_5m"] + row["cache_1h"] + row["cache_read"]


def cost_for(row: dict) -> float:
    in_rate, out_rate = PRICING[row["family"]]
    return (
        row["input"] * in_rate
        + row["output"] * out_rate
        + row["cache_5m"] * in_rate * CACHE_WRITE_5M
        + row["cache_1h"] * in_rate * CACHE_WRITE_1H
        + row["cache_read"] * in_rate * CACHE_READ
    ) / 1_000_000


def discover_transcripts(main_path: str) -> list:
    """Return the orchestrator transcript plus any subagent transcripts.

    Subagents are read from `<session>/subagents/agent-*.jsonl`, named via the
    sibling .meta.json.
    """
    items = [{"label": "main", "agent_type": "main", "description": None, "path": main_path}]
    sub_dir = os.path.join(main_path[:-6] if main_path.endswith(".jsonl") else main_path, "subagents")
    for jp in sorted(glob.glob(os.path.join(sub_dir, "agent-*.jsonl"))):
        agent_type, description = "subagent", None
        meta_path = jp[:-6] + ".meta.json"
        if os.path.exists(meta_path):
            try:
                meta = json.load(open(meta_path, encoding="utf-8"))
                agent_type = meta.get("agentType") or agent_type
                description = meta.get("description")
            except (OSError, json.JSONDecodeError):
                pass
        items.append({"label": agent_type, "agent_type": agent_type,
                      "description": description, "path": jp})
    return items


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--transcript", help="Path to the orchestrator session .jsonl")
    ap.add_argument("--json", action="store_true", help="Emit JSON instead of markdown")
    args = ap.parse_args()

    path = args.transcript or default_transcript()
    if not path or not os.path.exists(path):
        print("Token/cost report: no session transcript found.", file=sys.stderr)
        return 1

    unknown: set = set()
    agents = []
    for item in discover_transcripts(path):
        by_model, unk = aggregate_usage(item["path"])
        unknown |= unk
        if not by_model:
            continue
        models = sorted(by_model.values(), key=cost_for, reverse=True)
        agents.append({
            "agent": item["agent_type"],
            "description": item["description"],
            "models": models,
            "tokens": sum(tokens_in(r) for r in models),
            "cost": sum(cost_for(r) for r in models),
        })
    agents.sort(key=lambda a: a["cost"], reverse=True)

    total_tokens = sum(a["tokens"] for a in agents)
    total_cost = sum(a["cost"] for a in agents)

    if args.json:
        out = {
            "transcript": path,
            "total_tokens": total_tokens,
            "total_cost_usd": round(total_cost, 4),
            "agents": [
                {
                    "agent": a["agent"],
                    "role": display_name(a["agent"]),
                    "description": a["description"],
                    "total_tokens": a["tokens"],
                    "cost_usd": round(a["cost"], 4),
                    "models": [
                        {
                            "model": r["model"],
                            "turns": r["turns"],
                            "input_tokens": r["input"],
                            "output_tokens": r["output"],
                            "cache_write_5m_tokens": r["cache_5m"],
                            "cache_write_1h_tokens": r["cache_1h"],
                            "cache_read_tokens": r["cache_read"],
                            "total_tokens": tokens_in(r),
                            "cost_usd": round(cost_for(r), 4),
                        }
                        for r in a["models"]
                    ],
                }
                for a in agents
            ],
            "unknown_models": sorted(unknown),
        }
        print(json.dumps(out, indent=2))
        return 0

    t_in = sum(r["input"] for a in agents for r in a["models"])
    t_out = sum(r["output"] for a in agents for r in a["models"])
    t_cw = sum(r["cache_5m"] + r["cache_1h"] for a in agents for r in a["models"])
    t_cr = sum(r["cache_read"] for a in agents for r in a["models"])

    print("**Run cost (token spend)**")
    print()
    print("| Agent | Model | In | Out | Cache write | Cache read | Total | Cost |")
    print("|---|---|---:|---:|---:|---:|---:|---:|")
    for a in agents:
        label = display_name(a["agent"])
        desc = a["description"]
        if desc:
            desc = desc if len(desc) <= 60 else desc[:57] + "..."
            label += f" — {desc}"
        label = label.replace("|", "/")
        for r in a["models"]:
            print(
                f"| {label} | {r['model']} | {r['input']:,} | {r['output']:,} | "
                f"{r['cache_5m'] + r['cache_1h']:,} | {r['cache_read']:,} | "
                f"{tokens_in(r):,} | ${cost_for(r):,.2f} |"
            )
    print(
        f"| **Total** | | **{t_in:,}** | **{t_out:,}** | **{t_cw:,}** | "
        f"**{t_cr:,}** | **{total_tokens:,}** | **${total_cost:,.2f}** |"
    )
    if unknown:
        print(f"\n_Unpriced model(s) skipped: {', '.join(sorted(unknown))}._")
    print("\n_Excludes the final reporting turn(s)._")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
