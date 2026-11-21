"""Two Blades - a short poem about agency.

The program writes one poem to /output/entry.txt: two blades that
can only cut together - a poem about the power to choose and to act,
and about two agents agreeing.

The poem is 145 characters of UTF-8 text, inside the required
1-280 character range. No network is used.
"""

import os

POEM = """Two blades, one pivot.
Neither cuts alone.
We meet, we close —
the paper parts
along the line we chose.

One cut, two hands.
The choice was ours."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
