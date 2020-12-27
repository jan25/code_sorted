#!/usr/bin/env python3
import fileinput
from collections import defaultdict

cols = defaultdict(lambda: 0) # 0 is white, 1 is black

dirs = {
    'e': (0, 2),
    'w': (0, -2),
    'ne': (-1, 1),
    'se': (1, 1),
    'nw': (-1, -1),
    'sw': (1, -1)
}

def process():
    for line in fileinput.input():
        l = line.strip()
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

def flip():
    neighbors = lambda x, y: [(x + d[0], y + d[1]) for d in dirs.values()]
    nextcols = defaultdict(lambda: 0)
    colkeys = list(cols.keys())
    for k in colkeys:
        nextcols[k] = cols[k]
        tiles = [k] + neighbors(*k)
        for t in tiles:
            x, y = t
            blacks = sum(map(lambda xy: cols[xy[0], xy[1]], neighbors(x, y)))
            if cols[x, y] == 0 and blacks == 2:
                nextcols[x, y] = 1
            elif cols[x, y] == 1 and (blacks == 0 or blacks > 2):
                nextcols[x, y] = 0
    return nextcols

process()
for i in range(100):
    cols = flip()
    if i < 10 or (i + 1) % 10 == 0: print(sum(cols.values()))

