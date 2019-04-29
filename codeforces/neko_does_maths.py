from math import gcd

def lcm(a, b):
    return (a * b) // int(gcd(a, b))

def Solution(a, b):
    if a == b: return 0
    if a < b:
        a, b = b, a

    diff = a - b
    divs = []
    for d in range(1, diff + 2):
        if d * d > diff: break
        if diff % d == 0:
            divs.append(d)
            if d * d <= diff:
                divs.append(diff // d)

    min_lcm = lcm(a, b)
    ans = 0
    for i in divs:
        if a % i != b % i: continue
        l, k = 0, 0
        if a % i == 0:
            l = lcm(a + k, b + k)
            k = 0
        else:
            l = lcm((i - a % i) + a, (i - b % i) + b)
            k = (i - a % i)
        
        if l < min_lcm:
            ans = k
            min_lcm = l
    return ans
            

a, b = map(int, input().split())
print (Solution(a, b))