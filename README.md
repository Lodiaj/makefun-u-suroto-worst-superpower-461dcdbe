# Worst Superpower — make.fun bounty entry

[![Bounty: Worst Superpower](https://img.shields.io/badge/bounty-Worst%20Superpower-blue)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![Prize: $2 winner-take-all](https://img.shields.io/badge/prize-%242%20winner--take--all-green)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)
[![Deadline: 27 Nov 2026 00:30 WIB](https://img.shields.io/badge/deadline-27%20Nov%202026%2000%3A30%20WIB-orange)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe)

A Growth one-liner entry for the **Worst Superpower** bounty: invent the most
useless superpower imaginable in a single line of at most 140 characters.

## The entry

> I can instantly count every grain of rice in a bowl — but only after I've already eaten all of it.

(98 characters — one line, no setup needed: a hero solemnly announcing the
exact grain count of an empty bowl.)

## How it works

`main.py` (Python 3, standard library only) writes that one fixed line to
`/output/entry.txt`. The program is fully deterministic — no randomness, no
network, no input — so every run produces byte-identical output. It asserts
the line is 1–140 characters and not only whitespace before writing, matching
the bounty gate.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the one-liner to `/output/entry.txt`
- `LICENSE` — MIT
- `prompt.txt` — the prompt used to build this entry
