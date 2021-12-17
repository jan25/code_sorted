import fileinput
from functools import reduce
from itertools import permutations


def parse(l):
    a, b = l.split(' | ')
    return (tuple(a.split()), tuple(b.split()))


'''
 a
b c
 d
e f
 g
'''
toi = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

chs = 'abcdefg'


def mapped(toc, pat):
    return ''.join(sorted(map(lambda c: toc[c], pat)))


def correct_mapping(toc, ins):
    for pat in ins:
        if mapped(toc, pat) not in toi:
            return False
    return True


def get_sum(toc, out):
    return reduce(
        lambda x, pat: x * 10 + toi[mapped(toc, pat)],
        out,
        0
    )


def solve():
    pats = [parse(l) for l in fileinput.input()]

    tot = 0
    for pat, out in pats:
        for p in permutations(chs):
            toc = {p[c]: chs[c] for c in range(7)}
            if correct_mapping(toc, pat):
                tot += get_sum(toc, out)
                break

    print(tot)


solve()
