#!/usr/bin/python3
import fileinput
from collections import deque

a, b = [], []
lines = a
for line in fileinput.input():
    if line.strip() == "":
        a = lines
        lines = b
    elif line.strip().isdigit():
        lines.append(int(line.strip()))

print(a, b)

def score(a):
    return sum((i + 1) * val for i, val in enumerate(reversed(a)))

def rec_combat(a, b):
    a, b = deque(a), deque(b)
    aseen, bseen = set(), set()
    while a and b:
        if tuple(a) in aseen or tuple(b) in bseen:
            return score(a)
        aseen.add(tuple(a))
        bseen.add(tuple(b))
        ac, bc = a.popleft(), b.popleft()
        if ac <= len(a) and bc <= len(b):
            subgame = rec_combat(tuple(a)[:ac], tuple(b)[:bc])
            if subgame > 0:
                a.append(ac)
                a.append(bc)
            else:
                b.append(bc)
                b.append(ac)
        else:
            if ac > bc:
                a.append(ac)
                a.append(bc)
            else:
                b.append(bc)
                b.append(ac)
    if a: return score(a)
    return -1 * score(b)

print(rec_combat(tuple(a), tuple(b)))