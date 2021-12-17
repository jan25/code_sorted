import fileinput
from collections import defaultdict

lines = list(map(lambda s: s.strip(), fileinput.input()))

n, m = len(lines), len(lines[0])


def outside(i, j):
    return i < 0 or j < 0 or i >= n or j >= m


def adj(i, j):
    yield i + 1, j
    yield i, j + 1
    yield i - 1, j
    yield i, j - 1


def toi(i, j):
    return i * m + j


size = defaultdict(lambda: -1)


def root(i):
    if size[i] < 0:
        return i
    size[i] = root(size[i])
    return size[i]


def un(a, b):
    a, b = root(a), root(b)
    if a == b:
        return
    if size[a] > size[b]:
        a, b = b, a
    size[a] += size[b]
    size[b] = a


for i in range(n):
    for j in range(m):
        if int(lines[i][j]) == 9:
            continue
        for a, b in adj(i, j):
            if outside(a, b):
                continue
            if int(lines[a][b]) == 9 or int(lines[i][j]) == int(lines[a][b]):
                continue
            un(toi(a, b), toi(i, j))

sizes = sorted(map(abs, filter(lambda x: x < 0, size.values())))
print(sizes)
print(sizes[-3] * sizes[-2] * sizes[-1])
