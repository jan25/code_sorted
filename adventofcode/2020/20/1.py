#!/usr/bin/python3
import fileinput
from collections import defaultdict

images = []
image, n = [], 0
for l in fileinput.input():
    line = l.strip()
    if line == "":
        images.append((n, image))
        image = []
    elif 'Tile' in l:
        n = int(line.split()[1][:-1])
    else:
        image.append(line)

print(images)

def get_corners(tile):
    edges = []
    edges.append(tile[0][:])
    edges.append([])
    for i in range(10):
        edges[-1].append(tile[i][-1])
    edges.append(tile[-1][::-1])
    edges.append([])
    for i in range(10):
        edges[-1].append(tile[i][0])
    edges[-1].reverse()
    
    corners = []
    for i in range(4):
        a, b = edges[i], edges[(i + 1) % 4]
        corners.append((list(reversed(a)), b[:]))
    return corners

edges = defaultdict(int)
images = [[t[0], get_corners(t[1])] for t in images]
for _, corners in images:
    for a, b in corners:
        edges[tuple(a)] += 1
        edges[tuple(b)] += 1

prod = 1
for n, corners in images:
    for a, b in corners:
        if edges[tuple(a)] == 1 and edges[tuple(b)] == 1:
            prod *= n
            print('match', a, b)

print(prod)
