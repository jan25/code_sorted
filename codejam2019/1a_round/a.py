

def Solution(r, c):
    im = { 'result': 'IMPOSSIBLE' }
    po = { 'result': 'POSSIBLE' }

    path = []
    for i in range(0, r - 1, 2):
        for j in range(0, c - 2):
            path.append((i, j))
            path.append((i + 1, j + 2))


    po['path'] = path
    return po

def print_path(path):
    pass

for tc in range(int(input())):
    r, c = map(int, input())
    solution = Solution(r, c)
    print ('Case %d#: %s' % (tc + 1, solution['result']))
    if solution['result'] == 'POSSIBLE':
        print_path(solution['data'])