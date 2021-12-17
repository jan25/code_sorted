import fileinput

lines = list(map(lambda s: s.strip(), fileinput.input()))

point = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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
                return point[c]
            stk.pop()
        else:
            stk.append(c)
    return 0


print(sum(points(l) for l in lines))
