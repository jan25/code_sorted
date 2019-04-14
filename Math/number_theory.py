

def gcd(a, b):
    if a < b: a, b = b, a
    if b == 0: return a
    return gcd(b, a % b)

# Extended euclidean algorithm
# if inverse of a mod m
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
