import fileinput
from collections import defaultdict

pairs = [l.strip().split('-') for l in fileinput.input()]

graph = defaultdict(set)
for a, b in pairs:
    graph[a].add(b)
    graph[b].add(a)


def paths(node: str, seen: set[str]):
    if node == 'end':
        return 1

    if node.islower():
        if node in seen:
            return 0
        seen.add(node)

    p = sum(paths(n, seen) for n in graph[node])

    if node.islower():
        seen.remove(node)

    return p


print(paths('start', set()))
