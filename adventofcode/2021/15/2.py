import fileinput
from collections import defaultdict
import heapq

grid = [list(map(int, l.strip())) for l in fileinput.input()]
n, m = len(grid), len(grid[0])
print(n, m)

dist = defaultdict(lambda: float('inf'))
dist[5 * n - 1, 5 * m - 1] = 0


def neighs(i, j):
    for ni, nj in [[i + 1, j], [i, j + 1], [i - 1, j], [i, j - 1]]:
        if ni >= 0 and ni < 5 * n and nj >= 0 and nj < 5 * m:
            yield ni, nj


def val(i, j):
    v = grid[i % n][j % m]
    for _ in range(i // n + j // m):
        v += 1
        if v > 9:
            v %= 9
    return v


def risk():
    h = [(0, 5 * n - 1, 5 * m - 1)]
    while True:
        d, i, j = heapq.heappop(h)
        if i == 0 and j == 0:
            return d
        for ni, nj in neighs(i, j):
            if d + val(i, j) < dist[ni, nj]:
                dist[ni, nj] = d + val(i, j)
                heapq.heappush(h, (dist[ni, nj], ni, nj))


print(risk())
