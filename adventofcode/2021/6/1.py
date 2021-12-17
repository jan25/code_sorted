import fileinput
from functools import cache

line = next(fileinput.input())
fish = list(map(int, line.split(',')))


@cache
def how_many(f, d):
    if d == 0:
        return 1

    total = 0
    if f == 0:
        f = 6
        total = how_many(8, d - 1)
    else:
        f -= 1

    return total + how_many(f, d - 1)


print(sum(how_many(d, 80) for d in fish))
