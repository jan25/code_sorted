
def ok(cs, ds, l, r, k):
    cs_max = 0
    for i in range(l, r + 1):
        cs_max = max(cs_max, cs[i])
    ds_max = 0
    for i in range(l, r + 1):
        ds_max = max(ds_max, ds[i])
    if abs(cs_max - ds_max) <= k:
        return True
    return False

def Solution(cs, ds, n, k):
    lr = 0
    for i in range(n):
        for j in range(i, n):
            if ok(cs, ds, i, j, k):
                # print (i, j)
                lr += 1
    return lr

for t in range(int(input())):
    n, k = map(int, input().split())
    cs = list(map(int, input().split()))
    ds = list(map(int, input().split()))
    print ('Case #%d: %d' % (t + 1, Solution(cs, ds, n, k)))