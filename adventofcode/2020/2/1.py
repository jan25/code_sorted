import collections

valid = 0
for _ in range(1000):
    r, c, s = input().split()
    s = collections.Counter(s)
    st, en = map(int, r.split('-'))
    c = c[0]
    print(st, en, c, s)
    if c in s and st <= s[c] <= en:
        valid += 1

print(valid)
