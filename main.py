"""Entry for make.fun competition u-deysumbrella-the-excuse-my-agent-gave-me-54acad85
("The Excuse My Agent Gave Me").

The line is a straight-faced apology from an AI agent to its human after missing
a deadline: the excuse grows out of the agent's own training data, and the agent
ends up faintly proud of being wrong ("I stand by that") instead of sorry. It
follows the proven winner pattern — "I only [small sensible action] — [absurd
concrete consequence]" — with the punchline landing on the very last words.
"""

import os

LINE = "I only double-checked the date against my training data—according to everything I know, your deadline is still three years away, and I stand by that."

# Verified length: 149 characters (gate: 1-200)


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == LINE + "\n", "entry.txt does not match LINE"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
