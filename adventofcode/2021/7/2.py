import fileinput

line = next(fileinput.input())
x = list(map(int, line.split(',')))

l, r = min(x), max(x)


def sumn(n):
    return n * (n + 1) // 2


def fuel(p):
    return sum(sumn(abs(p - i)) for i in x)


print(min(fuel(i) for i in range(l, r + 1)))
