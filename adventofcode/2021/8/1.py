import fileinput
from itertools import chain


def parse(l):
    a, b = l.split(' | ')
    return (tuple(a.split()), tuple(b.split()))


pats = [parse(l) for l in fileinput.input()]

print(sum(1 for s in chain.from_iterable(p[1]
      for p in pats) if len(s) in (2, 4, 3, 7)))
