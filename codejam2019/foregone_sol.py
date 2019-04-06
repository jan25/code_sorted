
def print_sol(tc, a, b):
    a, b = int(a), int(b)
    if b == 0:
        a -= 1
        b += 1
    print ('Case #%d: %d %d' % (tc + 1, a, b))

def solve(tc, n):
    a, b = [], []
    while len(n) > 0:
        mod10 = n[-1]
        b.append('2' if mod10 == '4' else '0')
        a.append('2' if mod10 == '4' else mod10)
        n = n[:-1]
    print_sol(tc, ''.join(a[::-1]), ''.join(b[::-1]))

for tc in range(int(input())):
    solve(tc, input())