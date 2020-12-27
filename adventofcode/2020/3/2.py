grid = []

while True:
    try:
        grid.append(input())
    except Exception as e:
        break

def count_trees(dx, dy):
    x, y = 0, 0
    trees = 0
    while y < len(grid):
        if grid[y][x] == '#': trees += 1
        x = (x + dx) % len(grid[0])
        y += dy
    return trees

trees = 1
for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    trees *= count_trees(x, y)
print(trees)