
n = int(input())
students = [input() for _ in range(n)]

d = {chr(c): 0 for c in range(ord('a'), ord('z'))}
for s in students:
    if len(s) > 0: d[s[0].lower()] += 1

def _sum(n):
    if n < 2: return 0
    return n * (n - 1) // 2

pairs = 0
for k, v in d.items():
    h = v // 2
    pairs += _sum(h) + _sum(v - h)

print (pairs)