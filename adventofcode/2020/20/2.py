#!/usr/bin/python3
import fileinput
from collections import defaultdict, deque
from copy import deepcopy

images = []
image, n = [], 0
for l in fileinput.input():
    line = l.strip()
    if line == "":
        images.append(image)
        image = []
    elif 'Tile' in l:
        n = int(line.split()[1][:-1])
    else:
        image.append(list(line))

images.append(image)

def printimg(img):
    print('--------')
    for row in img:
        print(''.join(row))
    print('--------')

def rotate(img):
    n, m = len(img), len(img[0])
    rotated = [['.' for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated[j][n - 1 - i] = img[i][j]
    print('rotated')
    printimg(img)
    printimg(rotated)
    return rotated

def flip(img):
    n, m = len(img), len(img[0])
    flipped = [['.' for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            flipped[j][i] = img[i][j]
    return flipped

arrangs = []
for i in images:
    copy, arr = i, []
    for _ in range(4):
        copy = rotate(copy)
        flipped = flip(copy)
        arr += [deepcopy(copy), deepcopy(flipped)]
    assert copy == i
    assert len(arr) == 8
    arrangs.append(arr)

side = defaultdict(list)
down = defaultdict(list)

def match_side(a, b):
    n, m = len(a), len(a[0])
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    for i in range(n):
        if a[i][m - 1] != b[i][0]: return False
    return True

def match_down(a, b):
    n, m = len(a), len(a[0])
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    for i in range(m):
        if a[n - 1][i] != b[0][i]: return False
    return True

for i in range(len(images)):
    for j in range(len(images)):
        if i == j: continue
        for ii, imgi in enumerate(arrangs[i]):
            for jj, imgj in enumerate(arrangs[j]):
                if match_side(imgi, imgj):
                    side[i, ii].append((j, jj))
                if match_down(imgi, imgj):
                    down[i, ii].append((j, jj))

def get_corner(n, m):
    left = set()
    for i in range(len(images)):
        for ii in range(len(arrangs[i])):
            corner, l = (i, ii), 1
            while side[corner]:
                corner = side[corner][0]
                l += 1
            if l == m:
                left.add((i, ii))
    right = set()
    for p in left:
        corner, l = p, 1
        while down[corner]:
            corner = down[corner][0]
            l += 1
        if l == n:
            right.add(p)
    return right

n, m = int(len(images) ** 0.5), int(len(images) ** 0.5)

def make_grid():
    
    corners = get_corner(n, m)
    corner = corners.pop()

    # First row
    grid, row = [], [corner]
    for _ in range(m - 1):
        corner = side[corner][0]
        row.append(corner)
    grid.append(row)
    assert len(row) == m

    used = set([p[0] for p in row])
    # Remaining rows
    for _ in range(n - 1):
        row = []
        for e in grid[-1]:
            assert down[e]
            row.append(down[e][0])
        assert len(row) == m
        grid.append(row)
        used = used.union([p[0] for p in row])

    # Sanity checks
    assert len(used) == len(images)

    for i in range(n):
        for j in range(m):
            ii, jj = grid[i][j]
            grid[i][j] = arrangs[ii][jj]
            if i > 0:
                a, b = grid[i - 1][j], grid[i][j]
                assert match_down(a, b)
            if j > 0:
                a, b = grid[i][j - 1], grid[i][j]
                assert match_side(a, b)

    return grid

def remove_border(img):
    return [row[1:-1] for row in img][1:-1]

def concat(grid):
    concated = []
    for row in grid:
        for rows in zip(*row):
            val = ''.join(map(lambda v: ''.join(v), rows))
            concated.append(val)
    return concated


def remove_borders_and_concat(grid):
    for i in range(n):
        for j in range(m):
            grid[i][j] = remove_border(grid[i][j])
    return concat(grid)

monster = '''
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.split('\n')[1:]

def mark_monster(g):
    rows, cols = len(g), len(g[0])
    for i in range(rows - len(monster) + 1):
        for j in range(cols - len(monster[0]) + 1):
            match = True
            for k in range(len(monster)):
                for l in range(len(monster[0])):
                    if monster[k][l] == ' ': continue
                    if g[i + k][j + l] != '#': match = False
                    if not match: break
                if not match: break
            if not match: continue
            for k in range(len(monster)):
                for l in range(len(monster[0])):
                    if monster[k][l] == ' ': continue
                    g[i + k][j + l] = 'O'

g = make_grid()
g = remove_borders_and_concat(g)

for _ in range(4):
    g = rotate(g)
    mark_monster(g)
    g = flip(g)
    mark_monster(g)

print(sum(row.count('#') for row in g))