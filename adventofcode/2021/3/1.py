import fileinput
from functools import reduce

lines = list(l for l in fileinput.input())

counts = reduce(
    lambda cur, nex: [int(a) + int(b) for a, b in zip(cur, nex)],
    lines,
    '0' * len('000101000110')
)

gama = [int(2 * c > len(lines)) for c in counts]
eps = [b ^ 1 for b in gama]


def tostr(arr): return ''.join(map(str, arr))


print(int(f'0b{tostr(gama)}', 2) * int(f'0b{tostr(eps)}', 2))
