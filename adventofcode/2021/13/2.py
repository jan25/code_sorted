import fileinput
from collections import defaultdict

points = defaultdict(int)

inp = fileinput.input()

for l in inp:
    l = l.strip()
    if l == '':
        break
    a, b = map(int, l.split(','))
    points[a, b] += 1


def hor(v):
    new_keys = defaultdict(int)
    for a, b in points.keys():
        assert b != v
        if b > v and points[a, b] > 0:
            new_keys[(a, v - (b - v))] += 1
            points[a, b] = 0
    for k, v in new_keys.items():
        points[k] = v


def ver(v):
    new_keys = defaultdict(int)
    for a, b in points.keys():
        assert a != v
        if a > v and points[a, b] > 0:
            new_keys[(v - (a - v), b)] += 1
            points[a, b] = 0
    for k, v in new_keys.items():
        points[k] = v


for l in inp:
    i = l.strip().split()[-1]
    op, v = i.split('=')
    v = int(v)
    if op == 'x':
        ver(v)
    if op == 'y':
        hor(v)


x = max(x for x, y in points.keys() if points[x, y] > 0)
y = max(y for x, y in points.keys() if points[x, y] > 0)
print(x, y)
for j in range(y + 1):
    for i in range(x + 1):
        print('#' if points[i, j] > 0 else '.', sep='', end='')
    print()
