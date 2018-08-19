import sys
from functools import cmp_to_key

n, q = map(int, input().split())
ans = {chr(c): {} for c in range(ord('A'), ord('A') + n)}

def cmp(a, b):
    if b not in ans[a]:
        print ('?', a, b)
        sys.stdout.flush()
        lt = input()
        ans[a][b] = lt == '<'
        ans[b][a] = lt == '>'
    return ans[a][b]   

seq = [chr(c) for c in range(ord('A'), ord('A') + n)]
print('!', ''.join(sorted(seq, key=cmp_to_key(cmp))))
