grid = []

while True:
    try:
        grid.append(input())
    except Exception as e:
        break

x, y = 0, 0
trees = 0
while y < len(grid):
    if grid[y][x] == '#': trees += 1
    x = (x + 3) % len(grid[0])
    y += 1

print(trees)