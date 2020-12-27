#!/usr/bin/env python3
import bisect
import fileinput
import heapq
from collections import Counter, defaultdict, deque
from functools import lru_cache

grid = [list(l.strip()) for l in fileinput.input()]
n, m = len(grid), len(grid[0])

def sit():
    nextgrid = [row[:] for row in grid]
    for i in range(n):
        for j in range(m):
            if grid[i][j] not in {'L', '#'}: continue
            occupied = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ii, jj = i + di, j + dj
                    if i == ii and j == jj: continue
                    if ii < 0 or jj < 0 or ii >= n or jj >= m: continue
                    if grid[ii][jj] == '#': occupied += 1
            if grid[i][j] == '#' and occupied >= 4: nextgrid[i][j] = 'L'
            elif grid[i][j] == 'L' and occupied == 0: nextgrid[i][j] = '#'
    return nextgrid

while True:
    ng = sit()
    if ng == grid: break
    grid = ng

print(sum(row.count('#') for row in grid))