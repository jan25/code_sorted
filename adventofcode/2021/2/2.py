from functools import reduce
import fileinput


def dirs():
    aim = 0
    for line in fileinput.input():
        what, how = line.split()
        how = int(how)
        if what == 'forward':
            yield how, aim * how
        if what == 'up':
            aim -= how
        elif what == 'down':
            aim += how


hor, ver = reduce(
    lambda cur, nex: (cur[0] + nex[0], cur[1] + nex[1]),
    dirs()
)
print(hor, ver)
print(hor * ver)
