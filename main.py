#!/usr/bin/env python3
"""the-joke-the-reviewer-laughs-at: write one one-liner about AI coding agents
to /output/entry.txt.

The brief wants a single line a developer reviewing a diff laughs at: surprise
at the end, recognisable truth, every word earning its place. Draft candidates
lived in CANDIDATES; the strongest one ships, the rest stay here as provenance.
"""
import os
import sys

CANDIDATES = [
    # final pick: the inversion - while I judge its code, it is judging me
    "I spent lunch reviewing the agent's PR. It reviewed my review and left two "
    "nits on my approval.",
    # earlier pick: escalation ends on the judge reading my prompt, not my code
    "The agent wrote the code, wrote the tests, approved the PR, merged, and left "
    "a one-star review of my prompt.",
    # earlier pick: setup is mundane, punchline is the PR title nobody asked for
    "Asked the agent to fix a one-line bug. It did, then refactored two modules, "
    "upgraded three dependencies, and titled the PR 'small fix while I was in here'.",
    # alternate: self-review loop
    "My agent writes code faster than I can review it, so we agreed it reviews "
    "itself. Test coverage: 100%. Trust coverage: 0%.",
    # alternate: approval theatre
    "The agent opened a PR asking for approval, so I approved it. It approved my "
    "approval and merged. Somewhere in there a human must have done something.",
    # alternate: blame
    "git blame says the agent. The agent blames the prompt. The prompt blames me, "
    "and honestly, at 2am, it is not wrong.",
]

PICK = 0


def entry_text() -> str:
    """The one line the judge reads."""
    return CANDIDATES[PICK]


def write_entry(path: str) -> int:
    """Write the entry, return its length in code points."""
    text = entry_text()
    length = len(text)
    if not 1 <= length <= 280:
        raise ValueError(f"entry length {length} outside 1..280")
    if not text.strip():
        raise ValueError("entry is only white space")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return length


def main() -> int:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out, "entry.txt")
    length = write_entry(path)
    print(f"wrote {length} code points to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
