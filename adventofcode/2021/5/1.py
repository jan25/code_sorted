import fileinput


def parse_line(l):
    a, b = l.split(' -> ')
    return tuple(map(int, f'{a},{b}'.split(',')))


def add_line(x1, y1, x2, y2, grid):
    if (x1, y1) > (x2, y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    if x1 == x2:
        for y in range(y1, y2 + 1):
            grid[x1][y] += 1
        return
    if y1 == y2:
        for x in range(x1, x2 + 1):
            grid[x][y1] += 1


xys = [parse_line(l) for l in fileinput.input()]

grid = [[0] * 1000 for _ in range(1000)]
for x1, y1, x2, y2 in xys:
    assert max(x1, y1, x2, y2) < 1000
    assert not (x1 == x2 and y1 == y2)
    add_line(x1, y1, x2, y2, grid)

print(sum(int(cell > 1) for row in grid for cell in row))
