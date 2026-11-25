#!/usr/bin/env python3
"""Write one original excuse line to /output/entry.txt.

The line is the excuse an AI agent gives its human for a bug it shipped,
in the agent's own voice. The joke turns on something only an agent could
say: the agent did its due diligence and asked the model whether the code
was ready -- but the model it asked was itself, so the review was never
independent. The twist lands in the last three words.

The gate is checked here exactly as the sealed scorer states it:
UTF-8 text of 1 to 200 characters, not only white space, one line.
This line is 83 characters.
"""
import os

LINE = "I asked the model whether the code was ready before I shipped it. The model was me."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert LINE.strip(), "entry must not be only white space"
    assert LINE.count(".") == 2, "entry must be two short sentences"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
