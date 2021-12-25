
lx, ly = 207, -63
rx, ry = 263, -115


def out(x, y):
    return x > rx or y < ry


def hit(x, y):
    return x >= lx and x <= rx and y <= ly and y >= ry


def sim(vx, vy):
    maxh = 0
    x, y = 0, 0
    while not out(x, y):
        x += vx
        y += vy
        maxh = max(maxh, y)
        if hit(x, y):
            return maxh, True
        vy -= 1
        if vx > 0:
            vx -= 1
    return maxh, False


count = 0
for vx in range(270):
    for vy in range(-120, 120):
        _, ok = sim(vx, vy)
        count += int(ok)
print(count)
