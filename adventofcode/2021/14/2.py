import fileinput
import collections

lines = list(fileinput.input())

pairs = list(map(lambda x: tuple(x.strip().split(' -> ')), lines[2:]))

s = 'x' + lines[0].strip() + 'y'
count = collections.defaultdict(int)
for i in range(len(s) - 1):
    count[s[i: i + 2]] += 1

'''
 AB X CD

 count + BX
 split B Y X
'''


def step():
    c = collections.defaultdict(int)
    for a, b in pairs:
        if a not in count:
            continue
        c[a[0] + b] += count[a]
        c[b + a[1]] += count[a]
        del count[a]
    for k, v in c.items():
        count[k] += v


for _ in range(40):
    step()

chars = collections.defaultdict(int)
for k, v in count.items():
    if k[0] == 'x':
        chars[k[1]] += 2
    elif k[1] == 'y':
        chars[k[0]] += 2
    else:
        chars[k[0]] += v
        chars[k[1]] += v

print(count)
print(chars)

print((max(chars.values()) - min(chars.values())) // 2)
