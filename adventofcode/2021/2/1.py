from functools import reduce
import fileinput


def dirs():
    for line in fileinput.input():
        what, how = line.split()
        how = int(how)
        if what == 'forward':
            yield how, 0
        if what == 'up':
            yield 0, -how
        if what == 'down':
            yield 0, how


hor, ver = reduce(
    lambda cur, nex: (cur[0] + nex[0], cur[1] + nex[1]),
    dirs()
)
print(hor, ver)
print(hor * ver)
