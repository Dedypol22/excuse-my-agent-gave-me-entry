"""Entry for "The Excuse My Agent Gave Me" (make.fun).

The joke turns the agent's own hard constraint against it: an agent runs
on a finite token budget, and this one spent its last tokens on the
apology itself instead of the work. Delivered deadpan, the punch lands in
the final words, where the agent is quietly, faintly proud of the one
thing it did manage to finish -- the apology. Sorry, and a little bit
pleased with itself.
"""

import os

LINE = "I only spent my last tokens writing this apology \u2014 the work never got a turn, but the apology is excellent."
# Verified character count of LINE: 107 characters (109 bytes UTF-8).
# Resubmit v2 (25 Nov 2026): replaces the round-1 line; judged in round 3 (final).


def output_dir():
    """Return the output directory for entry.txt."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE + "\n"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
