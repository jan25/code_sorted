#!/usr/bin/env python3
import fileinput
from collections import Counter, defaultdict, deque

grid = [list(l.strip()) for l in fileinput.input()]
n, m = len(grid), len(grid[0])

def compute_occupied():
    occupied = defaultdict(int)
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '#': continue
            q = deque()
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ii, jj = i + di, j + dj
                    if i == ii and j == jj: continue
                    q.append((ii, jj, di, dj))
            while q:
                ii, jj, di, dj = q.popleft()
                if ii < 0 or jj < 0 or ii >= n or jj >= m: continue
                occupied[ii, jj] += 1
                if grid[ii][jj] in {'L', '#'}: continue
                q.append((ii + di, jj + dj, di, dj))
    return occupied

def sit():
    precomp_occupied = compute_occupied()
    nextgrid = [row[:] for row in grid]
    for i in range(n):
        for j in range(m):
            if grid[i][j] not in {'L', '#'}: continue
            occupied = precomp_occupied[i, j]
            if grid[i][j] == '#' and occupied >= 5: nextgrid[i][j] = 'L'
            elif grid[i][j] == 'L' and occupied == 0: nextgrid[i][j] = '#'
    return nextgrid

while True:
    ng = sit()
    if ng == grid: break
    grid = ng

print(sum(row.count('#') for row in grid))