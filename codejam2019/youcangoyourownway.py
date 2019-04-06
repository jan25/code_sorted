import sys

def Solver(n, path):

    cells = set()
    def add_neighbors(x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                xx, yy = x + dx, y + dy
                if xx < n and yy < n and xx >= 0 and yy >= 0:
                    cells.add((xx, yy))

    taken = set() # taken edges

    x, y = 0, 0
    for c in path:
        xx, yy = x, y
        if c == 'S': xx += 1
        else: yy += 1
        taken.add((x, y, xx, yy))
        add_neighbors(xx, yy)
        x, y = xx, yy

    graph = {}
    def add_edge(x, y, xx, yy):
        if (x, y) not in graph:
            graph[(x, y)] = []
        graph[(x, y)].append((xx, yy))

    def add_edges(cell):
        x, y = cell
        # east
        xx, yy = x + 1, y
        if (x, y, xx, yy) not in taken and xx < n:
            add_edge(x, y, xx, yy)
        # zuid
        xx, yy = x, y + 1
        if (x, y, xx, yy) not in taken and yy < n:
            add_edge(x, y, xx, yy)

    for c in cells: add_edges(c)

    # print (graph)

    # now we have good enough graph to work with
    pars = {} # store parents of a cell in a path

    # BFS
    q, qi = [(0, 0)], 0
    while qi < len(q):
        c = q[qi]; qi += 1
        if c not in graph: continue
        for neighbor in graph[c]:
            if neighbor in pars: continue
            pars[neighbor] = c
            q.append(neighbor)

    # compute path using parents
    x, y = n - 1, n - 1
    path = []
    while x >= 0 and y >= 0:
        if (x, y) not in pars: break
        xx, yy = pars[(x, y)]
        if x == xx: path.append('E')
        else: path.append('S')
        x, y = xx, yy

    return ''.join(path[::-1])

for tc in range(int(input())):
    n, p = int(input()), input()
    print ('Case #%d: %s' % (tc + 1, Solver(n, p)))