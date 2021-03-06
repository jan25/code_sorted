#!/usr/bin/env python3
import fileinput
from collections import defaultdict

lines = []
for l in fileinput.input():
    lines.append(l.strip())

grid = defaultdict(lambda: '.')
for x, l in enumerate(lines):
    for y, ch in enumerate(l):
        grid[x, y, 1, 1] = ch

def neighbors(x, y, z, a, exclude=True):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for da in [-1, 0, 1]:
                    if exclude and sum(map(abs, [dx, dy, dz, da])) == 0: continue
                    yield x + dx, y + dy, z + dz, a + da

def count_active(g, x, y, z, a):
    active = 0
    for nx, ny, nz, na in neighbors(x, y, z, a):
        if g[nx, ny, nz, na] == '#': active += 1
    return active

def cycle(grid):
    nextgrid = defaultdict(lambda: '.')
    items = list(grid.keys())
    for coords in items:
        for x, y, z, a in list(neighbors(*coords, False)):
            active = count_active(grid, x, y, z, a)
            ch = grid[x, y, z, a]
            if ch == '#':
                if active in [2, 3]:
                    nextgrid[x, y, z, a] = '#'
            elif ch == '.':
                if active == 3: nextgrid[x, y, z, a] = '#'
    return nextgrid

for _ in range(6):
    grid = cycle(grid)

print(list(grid.values()).count('#'))
