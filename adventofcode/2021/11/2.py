import fileinput
from collections import deque

grid = [list(map(int, l.strip())) for l in fileinput.input()]
n, m = len(grid), len(grid[0])


def neighs(i, j):
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if ni >= 0 and nj >= 0 and ni < n and nj < m:
                yield ni, nj


def fill(i, j):
    q = deque()
    q.append((i, j))
    grid[i][j] = 0
    while q:
        i, j = q.popleft()
        for ni, nj in neighs(i, j):
            if grid[ni][nj] == 0:
                continue

            grid[ni][nj] += 1
            if grid[ni][nj] > 9:
                grid[ni][nj] = 0
                q.append((ni, nj))


def step():
    for row in grid:
        for i in range(len(row)):
            row[i] += 1

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val > 9:
                fill(i, j)

    return sum(row.count(0) for row in grid) == n * m


for s in range(1000):
    if step():
        print(s + 1)
        exit(0)
