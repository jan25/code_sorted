from typing import List
import fileinput
from functools import reduce


def chr_prio(c: str) -> int:
    if c.islower():
        return 1 + ord(c) - ord('a')
    return 26 + chr_prio(c.lower())


groups = []


def group_prio(group: List[str]) -> int:
    print(group)
    g1 = reduce(lambda a, b: set(a).intersection(set(b)), set(groups[:3]))
    g2 = reduce(lambda a, b: set(a).intersection(set(b)), set(groups[3:]))
    a, b = g1, g2
    print(a, b)
    assert len(a) > 0, f'a={a} is empty'
    assert len(b) > 0, f'b={b} is empty'
    print(list(a))
    return chr_prio(list(a)[0]) + chr_prio(list(b)[0])


prios = 0
for l in fileinput.input():
    groups.append(l.strip())
    if len(groups) == 6:
        prios += group_prio(groups)
        groups = []

print(prios)
