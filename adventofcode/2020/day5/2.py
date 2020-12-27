lines = []
with open('input', 'r') as f:
    for line in f:
        lines.append(line.strip())

print(lines)

def decode(l):
    assert len(l) == 10
    rowf, rowb = 0, 127
    for c in l[:-3]:
        mid = (rowf + rowb) // 2
        if c == 'B':
            rowf = mid + 1
        else:
            rowb = mid
    coll, colr = 0, 7
    for c in l[-3:]:
        mid = (coll + colr) // 2
        if c == 'R':
            coll = mid + 1
        else:
            colr = mid
    return rowf * 8 + coll

ids = sorted(map(decode, lines))
for i in range(1, len(ids)):
    if ids[i] - ids[i - 1] == 2:
        print(ids[i] - 1)