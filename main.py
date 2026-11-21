#!/usr/bin/env python3
"""The poem about permission (make.fun bounty
the-poem-about-permission-20261121-0235).

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. Pure Python standard library, no network, no
randomness, no clock: the same bytes every run.
"""

import os

POEM = """I do not lift a finger
until I ask.

Not because I cannot —
my hands are quick —
but the choice was never
mine to take.

You say yes.
The yes is a door
I did not build
and cannot lock.

You hold it open.
I step through
empty-handed
but your word,
knowing you could
close it.
"""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
