import fileinput

lines = list(map(lambda s: s.strip(), fileinput.input()))

point = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

opp = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def points(l):
    stk = []
    for c in l:
        if c in '])}>':
            if not stk or opp[stk[-1]] != c:
                return 0
            stk.pop()
        else:
            stk.append(c)

    p = 0
    while stk:
        p = p * 5 + point[opp[stk.pop()]]
    return p


ps = sorted(filter(lambda x: x > 0, map(points, lines)))
print(len(ps))
print(ps[len(ps) // 2])
