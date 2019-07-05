x = int(input())
res = False
for b in range(1, x + 1):
    for a in range(b, x + 2, b):
        if a * b > x and a // b < x:
            res = (a, b)
if res: print('%d %d' %(res[0], res[1]))
else: print(-1)