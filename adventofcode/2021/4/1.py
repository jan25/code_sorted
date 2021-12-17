import fileinput

lines = list(l for l in fileinput.input())


def mark(grid, n):
    s = 0
    for i in range(5):
        for j in range(5):
            if grid[i][j] == n:
                grid[i][j] = -1
            if grid[i][j] != -1:
                s += grid[i][j]
    for i in range(5):
        if grid[i].count(-1) == 5:
            return s
        if sum(int(grid[j][i] == -1) for j in range(5)) == 5:
            return s


def main():
    nums = list(map(int, lines[0].split(',')))

    grids = []
    for i in range(2, len(lines), 6):
        grid = []
        for j in range(i, i + 5):
            grid.append(list(map(int, lines[j].strip().split())))
        grids.append(grid)

    assert len(grids) == 100

    for n in nums:
        for g in grids:
            assert len(g) == 5
            for col in g:
                assert len(col) == 5
            score = mark(g, n)
            if score:
                print(g)
                print(n, score)
                print(n * score)
                exit(0)


main()
