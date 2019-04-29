'''
d   c

a   b
# '''
# def Solution(dirs, p, q):
#     a, b, c, d = [0, 0], [q, 0], [q, q], [0, q]
#     for dir in dirs:
#         direction = dir[2]
#         x, y = int(dir[0]), int(dir[1])
#         if direction == 'N' and a[1] <= y:
#             a[1] = b[1] = y + 1
#         if direction == 'S' and d[1] >= y:
#             d[1] = c[1] = y - 1

#         if direction == 'E' and a[0] <= x:
#             a[0] = d[0] = x + 1
#         if direction == 'W' and b[0] >= x:
#             c[0] = b[0] = x - 1

#         print (a, b, c, d)
    
#     return a

# def Solution(pers, p, q):
#     grid = [[0] * q + 1 for _ in range(q + 1)]
#     for d in dirs:
#         dir = d[2]
#         if dir == 'N':
#             for y in range(len(grid)):
#                 for x in range(len(grid[0])):
#                     if y > dir[1]:
#                         grid[x][y]

def Solution(pers, p, q):
    ns = [0] * (q + 1)
    ew = [0] * (q + 1)
    for d in pers:
        direction = d[2]
        x, y = d[0], d[1]

        if direction == 'N':
            ns[y + 1] += 1
        if direction == 'S':
            ns[0] += 1
            ns[y] -= 1
            
        if direction == 'E':
            ew[x + 1] += 1
        if direction == 'W':
            ew[0] += 1
            ew[x] -= 1
    
    for i in range(1, len(ns)):
        ns[i] += ns[i - 1]
    for i in range(1, len(ew)):
        ew[i] += ew[i - 1]
    # print (ns)
    # print (ew)
    
    x, y = 0, 0
    xval, yval = 0, 0
    for i, n in enumerate(ns):
        if n > yval:
            yval = n
            y = i
    for i, e in enumerate(ew):
        if e > xval:
            xval = e
            x = i

    return [x, y]


for t in range(int(input())):
    pers, q = map(int, input().split())
    ps = [input().split() for _ in range(pers)]
    for p in ps:
        p[0], p[1] = int(p[0]), int(p[1])
    sol = Solution(ps, pers, q)
    print ('Case #%d: %d %d' % (t + 1, sol[0], sol[1]))