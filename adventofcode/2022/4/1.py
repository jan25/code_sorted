import fileinput


def parse():
    for l in fileinput.input():
        a, b = l.strip().split(',')
        a = list(int(x) for x in a.split('-'))
        b = list(int(x) for x in b.split('-'))
        yield tuple(a), tuple(b)


def is_overlap(a, b) -> int:
    l, r = min(a[0], b[0]), max(a[1], b[1])
    return 1 if (l, r) in {a, b} else 0


print(sum(is_overlap(a, b) for a, b in parse()))
