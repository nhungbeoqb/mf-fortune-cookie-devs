"""Fortune Cookie Wisdom for Developers.

Writes one original line of fortune-cookie wisdom for a software
developer (at most 120 characters) to /output/entry.txt.

Candidates considered (5, genuinely different):
  A. The merge conflict you fear is two good ideas arriving at the
     same line.
     -- CHOSEN: reads like a real fortune cookie (one balanced
     sentence, one breath, addressed to "you"), true about a dev's
     day (merge conflicts), and turns the dreaded thing into
     something almost kind: a conflict is two GOOD ideas, not a
     mistake. Quiet double meaning on "the same line" (one line of
     code / one line of an argument / two minds arriving at the same
     conclusion). Concrete embodied scene: two changes landing on
     one line.
  B. The stack trace you ignore is the only witness that stayed to
     the end. -- Poetic, but "witness" is cleverness for its own
     sake; the scene is thinner than A's.
  C. The refactor you keep postponing is the bug report your future
     self already filed. -- Good double meaning on "filed", but the
     setup ("refactor you keep postponing") is a familiar complaint.
  D. Staging lies to you kindly; production tells the truth at 3 a.m.
     -- Two-beat aphorism, but reads as an observation, not a
     fortune; no quiet twist on a second read.
  E. The TODO you wrote for later has outlived the team that wrote
     it. -- Wry and true, but the twist is a shrug, not a double
     meaning.

v1: "The merge conflict you fear is two good ideas arriving at the
same line." (72 chars)
v2 (genuine second-round revision): "fear" -> "dread" -- "dread" is
the tired senior engineer's word: heavier, slower, more resigned
than "fear", and it makes the turn land harder (what you dread is
not a mistake, it is two good ideas). One char longer: 73 chars.
"""

import os

# The fortune, assembled from named parts so each clause reads on its own.
SUBJECT = "The merge conflict you dread "
PAYOFF = "is two good ideas "
PUNCH = "arriving at the same line."

ENTRY = SUBJECT + PAYOFF + PUNCH


def write_entry(text: str) -> None:
    """Write the fortune to the gate file, exactly one line + newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
