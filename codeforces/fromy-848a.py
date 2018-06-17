k = int(input())
tellingen = {}

c = ord('a')
for n in range(10**5, 0, -1):
    sum_n = n * (n + 1) // 2
    if sum_n <= k:
        k -= sum_n
        tellingen[c] = n + 1
        c += 1

cs = []
for c in tellingen:
    for i in range(tellingen[c]):
        cs.append(chr(c))
if len(cs) == 0: cs.append('z'):w:
iiprint (''.join(cs)) 
