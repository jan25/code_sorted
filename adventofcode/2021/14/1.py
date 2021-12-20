import fileinput
import collections

lines = list(fileinput.input())
s = lines[0].strip()
pairs = list(map(lambda x: tuple(x.strip().split(' -> ')), lines[2:]))


def step(s):
    at = dict()
    for a, b in pairs:
        for i in range(len(s)):
            if s[i: i + 2] == a:
                at[i] = b

    return ''.join((c + at[i]) if i in at else c for i, c in enumerate(s))


for _ in range(10):
    s = step(s)
    print(s)

count = collections.Counter(s)
mi, ma = min(count.values()), max(count.values())
print(len(s))
print(ma - mi)
