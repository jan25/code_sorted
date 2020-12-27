#!/usr/bin/env python3
import fileinput

lines = [l.strip() for l in fileinput.input()]

move = {
    'E': (1, 0),
    'W': (-1, 0),
    'N': (0, 1),
    'S': (0, -1)
}

wp = {
    'E': 10,
    'N': 1,
    'W': 0,
    'S': 0
}
rotated = ['E', 'N', 'W', 'S']

dirs = []
for l in lines:
    d = l[0]
    val = int(l[1:])
    dirs.append((d, val))

x, y = 0, 0
for d in dirs:
    m, val = d
    if m == 'F':
        for k, v in wp.items():
            x += move[k][0] * v * val
            y += move[k][1] * v * val
    elif m in {'N', 'E', 'W', 'S'}:
        wp[m] += val
    elif m in {'L', 'R'}:
        assert val % 90 == 0
        if m == 'R': val *= -1
        val = (val + 360) // 90
        nextwp = {}
        for i in range(4):
            j = (val + i) % 4
            nextwp[rotated[j]] = wp[rotated[i]]
        wp = nextwp
        rotated = rotated[val:] + rotated[:val]
    else: assert False

print(abs(x) + abs(y))