import fileinput
from collections import defaultdict

points = defaultdict(int)

inp = fileinput.input()

x, y = 0, 0
for l in inp:
    l = l.strip()
    if l == '':
        break
    a, b = map(int, l.split(','))
    x = max(x, a)
    y = max(y, b)
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
    break

print(sum(1 for a, b in points.keys() if points[a, b] > 0))
