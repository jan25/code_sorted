import fileinput
from collections import defaultdict
import heapq

grid = [list(map(int, l.strip())) for l in fileinput.input()]
n, m = len(grid), len(grid[0])

dist = defaultdict(lambda: float('inf'))
dist[n - 1, m - 1] = 0


def neighs(i, j):
    for ni, nj in [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
        if ni >= 0 and ni < n and nj >= 0 and nj < m:
            yield ni, nj


def risk():
    h = [(0, n - 1, m - 1)]
    while True:
        d, i, j = heapq.heappop(h)
        if i == 0 and j == 0:
            return d
        for ni, nj in neighs(i, j):
            if d + grid[i][j] < dist[ni, nj]:
                dist[ni, nj] = d + grid[i][j]
                heapq.heappush(h, (dist[ni, nj], ni, nj))


print(risk())
