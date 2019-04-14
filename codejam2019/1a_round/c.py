import sys

def _flush():
    sys.stdout.flush()

def Solution(n, m):
    max_seen = 0
    for _ in range(n):
        before = ['18' for _ in range(18)]
        print (' '.join(before)); _flush()
        after = list(map(int, input().split()))
        diff = 0
        for i in range(18): diff += after[i]
        max_seen = max(diff, max_seen)
    print (max_seen); _flush()
    int(input())

def mod_inv(a, m):
    mod = m
    if a < m: a, m = m, a
    p = [0, 1]
    q = []
    while True:
        if len(q) > 1:
            p.append((mod + p[-2] - p[-1] * q[-2]) % mod)
        if m == 0: break
        q.append(a // m)
        a, m = m, a % m
    return p[-1]

# x = a mod m
def find_x(a, m):
    M = 1
    for mod in m: M *= mod
    total_mod = 0
    for i in range(len(a)):
        total_mod += a[i] * (M // m[i]) * mod_inv(M // m[i], m[i])
    return total_mod % M

def Solution2(n, m):
    blades = [5, 7, 9, 11, 13, 16, 17]
    mods = []
    for i in range(n):
        before = [blades[i]] * 18
        print (' '.join([str(b) for b in before])); _flush()
        after = list(map(int, input().split()))
        diff = 0
        for j in range(18):
            diff += after[j] - before[j] + (18 if after[j] < before[j] else 0)
        mods.append(diff % blades[i])
    print (find_x(mods, blades)); _flush()

t, n, m = map(int, input().split())
for _ in range(t):
    if n == 7: Solution2(n, m)
    else: Solution(n, m)
