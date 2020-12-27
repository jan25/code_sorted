#!/usr/bin/env python3
import fileinput
from collections import Counter, defaultdict, deque

cols = defaultdict(lambda: 0) # 0 is white, 1 is black

dirs = {
    'e': (0, 2),
    'w': (0, -2),
    'ne': (-1, 1),
    'se': (1, 1),
    'nw': (-1, -1),
    'sw': (1, -1)
}

def process(l):
    i = 0
    x, y = 0, 0
    while i < len(l):
        if l[i] in dirs:
            x += dirs[l[i]][0]
            y += dirs[l[i]][1]
            i += 1
        elif l[i:i + 2] in dirs:
            x += dirs[l[i:i + 2]][0]
            y += dirs[l[i:i + 2]][1]
            i += 2
        else:
            assert False
    cols[x, y] = (cols[x, y] + 1) % 2

for l in fileinput.input():
    process(l.strip())

print(sum(cols.values()))
