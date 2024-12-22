import fileinput


def parse():
    for l in fileinput.input():
        a, b = l.strip().split(',')
        a = list(int(x) for x in a.split('-'))
        b = list(int(x) for x in b.split('-'))
        yield tuple(a), tuple(b)


def is_overlap(a, b) -> int:
    l, r = max(a[0], b[0]), min(a[1], b[1])
    return 0 if l > r else 1


print(sum(is_overlap(a, b) for a, b in parse()))
