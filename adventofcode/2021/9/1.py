import fileinput

lines = list(map(lambda s: s.strip(), fileinput.input()))

n, m = len(lines), len(lines[0])


def outside(i, j):
    return i < 0 or j < 0 or i >= n or j >= m


def adj(i, j):
    yield i + 1, j
    yield i, j + 1
    yield i - 1, j
    yield i, j - 1


def risk(i, j):
    for a, b in adj(i, j):
        if outside(a, b):
            continue
        if int(lines[a][b]) <= int(lines[i][j]):
            return 0

    return 1 + int(lines[i][j])


tot = 0
for i in range(n):
    for j in range(m):
        tot += risk(i, j)

print(tot)
