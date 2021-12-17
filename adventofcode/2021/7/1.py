import fileinput

line = next(fileinput.input())
x = list(map(int, line.split(',')))

l, r = min(x), max(x)


def fuel(p):
    return sum(abs(p - i) for i in x)


print(min(fuel(i) for i in range(l, r + 1)))
