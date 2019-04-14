'''
author:         areddy
created on:     12 04 2019
'''
def Solution(r, c, h, v, grid):
    im = 'IMPOSSIBLE'
    po = 'POSSIBLE'

    count_chocs = 0
    for row in grid:
        for cell in row:
            if cell == '@':
                count_chocs += 1
    
    count_pieces = (h + 1) * (v + 1)
    if count_chocs % count_pieces != 0:
        return im
    each = count_chocs // count_pieces
    if each == 0: return po

    ds = [[0] * c for _ in range(r)]
    for ri in range(r):
        c_sum = 0
        for ci in range(c):
            if grid[ri][ci] == '@':
                c_sum += 1
            ds[ri][ci] = c_sum + (ds[ri - 1][ci] if ri > 0 else 0)

    def get_sum(a, b, x, y):
        cell_sum = ds[x][y]
        if a >= 0 and b >= 0: cell_sum += ds[a][b]
        if a >= 0: cell_sum -= ds[a][y]
        if b >= 0: cell_sum -= ds[x][b]
        return cell_sum

    # vertical splits
    verticals = []
    until_last_c_sum = 0
    for ci in range(c):
        if ds[r - 1][ci] - until_last_c_sum == each * (h + 1):
            verticals.append(ci)
            until_last_c_sum = ds[r - 1][ci]
    
    # horizontal splits
    horizontals = []
    until_last_r_sum = 0
    for ri in range(r):
        if ds[ri][c - 1] - until_last_r_sum == each * (v + 1):
            horizontals.append(ri)
            until_last_r_sum = ds[ri][c - 1]

    if len(verticals) != v + 1 or len(horizontals) != h + 1:
        return im
    
    def check_split(a, b, x, y):
        return get_sum(a - 1, b - 1, x, y) == each
    
    last_h, last_v = 0, 0
    for hor in horizontals:
        last_v = 0
        for ver in verticals:
            if not check_split(last_h, last_v, hor, ver):
                return im
            last_v = ver + 1
        last_h = hor + 1

    return po

for tc in range(int(input())):
    r, c, h, v = map(int, input().split())
    grid = [input() for _ in range(r)]
    print ('Case #%d: %s' % (tc + 1, Solution(r, c, h, v, grid)))

