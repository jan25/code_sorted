#!/usr/bin/env python3
import fileinput

lines = [l.strip() for l in fileinput.input()]

move = {
    'E': (1, 0),
    'W': (-1, 0),
    'N': (0, 1),
    'S': (0, -1)
}

deg = {
    'E': 0,
    'W': 180,
    'N': 90,
    'S': 270
}
revdeg = {v: k for k, v in deg.items()}

dirs = []
for l in lines:
    d = l[0]
    val = int(l[1:])
    dirs.append((d, val))

face = 'E'
x, y = 0, 0
for d in dirs:
    m, val = d
    if m == 'F':
        diff = move[face]
        x += diff[0] * val
        y += diff[1] * val
    elif m in {'N', 'E', 'W', 'S'}:
        diff = move[m]
        x += diff[0] * val
        y += diff[1] * val
    elif m in {'L', 'R'}:
        assert val % 90 == 0
        diff = deg[face]
        if m == 'L': diff += val
        else: diff -= val
        diff = (diff + 360) % 360
        face = revdeg[diff]
    else: assert False
    print(x, y, face)

print(abs(x) + abs(y))