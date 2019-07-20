def pad(c):
    if c not in '{,}': return '{%s}' % c
    return c

def mul(a, b):
    return [i + j for i in a for j in b]

def solve_leq(ops, vals, n):
    assert n > 0
    loc_vals = [vals.pop() for _ in range(n + 1)]
    loc_ops = [ops.pop() for _ in range(n)]
    loc_ops.reverse()
    feq = [loc_vals.pop()]
    for i, op in enumerate(loc_ops):
        assert op in '+x'
        if op == '+':
            feq.append(loc_vals.pop())
        elif op == 'x':
            feq[-1] = mul(feq[-1], loc_vals.pop())
    for i in range(1, len(feq)):
        feq[0] += feq[i]
    return feq[0]

def solve(s):
    s = ''.join(list(map(pad, '{' + s + '}')))
    vals, ops = [], []
    clos = []
    prev_c = '-'
    for c in s:
        if c == '{':
            if prev_c not in '-{,': # mul-op
                ops.append('x')
                if len(clos) > 0: clos[-1] += 1
            clos.append(0)
        elif c == ',':
            ops.append('+')
            clos[-1] += 1
        elif c == '}':
            n_ops = clos.pop()
            if n_ops > 0:
                vals.append(solve_leq(ops, vals, n_ops))
        else:
            vals.append([c])
        prev_c = c

    return sorted(list(set(vals[-1])))

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        return solve(expression)
