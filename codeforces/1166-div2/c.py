
def findLowestX(a, si):
    l, r = 0, si
    while l < r:
        m = (l + r) // 2
        if a[si] - a[m] <= a[si]:
            r = m
        else: l = m + 1
    return l

def Solution(n, a):
    a.sort()
    pairs = 0
    for s in range(1, n):
        f = findLowestX(a, s)
        pairs += s - f
    return pairs

n = int(input())
a = list(map(int, input().split()))
print (Solution(n, a))
