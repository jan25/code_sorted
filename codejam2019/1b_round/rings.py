import sys

def _flush():
    sys.stdout.flush()

'''
{{1/10, -1/10, -1/20, 0, 0, 1/40}
{-6/5, 6/5, 1/10, 0, 0, -1/20}
{-2/5, -3/5, 6/5, 0, 0, -1/10}
{8/5, -8/5, -4/5, 1, 0, -1/10}
{-8/5, 8/5, 4/5, -1, 1, -2/5}
{12/5, -2/5, -6/5, 0, -1, 3/5}}
'''
mat = [
    [4, -4, -2, 0, 0, 1],
    [-48, 48, 4, 0, 0, -2],
    [-16, -24, 48, 0, 0, -4],
    [64, -64, -32, 40, 0, -4],
    [-64, 64, 32, -40, 40, -16],
    [96, -16, -48, 0, -40, 24]
]


def calculate(n):
    ns = []
    for j in range(6):
        mul = 0
        for i, x in enumerate(n):
            mul += mat[j][i] * x
        mul = mul // 40
        ns.append(mul)
    return ns

'''
22 26 33 49 70 122
'''
t, w = map(int, input().split())
for tc in range(t):
    n = []
    for i in range(6):
        print (i + 1); _flush()
        n.append(int(input()))
    ns = calculate(n)
    print (*ns); _flush()
