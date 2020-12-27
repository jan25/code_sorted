import collections

valid = 0
for _ in range(1000):
    r, c, s = input().split()
    st, en = map(int, r.split('-'))
    c = c[0]
    print(st, en, c, s)
    if not (st <= len(s) and en <= len(s)): continue
    if s[st - 1] == c and s[en - 1] == c: continue
    if s[st - 1] == c or s[en - 1] == c:
        valid += 1

print(valid)
