import fileinput
from collections import defaultdict

pairs = [l.strip().split('-') for l in fileinput.input()]

graph = defaultdict(set)
for a, b in pairs:
    graph[a].add(b)
    graph[b].add(a)


def printer(fn):
    def wrapper(*args):
        p = args[1].copy()
        res = fn(*args)
        if res == 1:
            print(p, args[0])
        return res
    return wrapper


@printer
def paths(node: str, path: list[str], allow: str):
    if node == 'end':
        if path.count(allow) == 2:
            return 1
        return int(allow == '-')

    if node.islower():
        if node != allow and path.count(node) > 0:
            return 0
        if node == allow and path.count(node) > 1:
            return 0

    path.append(node)

    p = sum(paths(n, path, allow) for n in graph[node])

    path.pop()

    return p


print(paths('start', [], '-') + sum(paths('start', [], n)
      for n in graph.keys() if n not in {'start', 'end'} and n.islower()))
