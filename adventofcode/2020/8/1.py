
insts = []
with open('input') as f:
    for inst in f:
        name, val = inst.split()
        insts.append((name, int(val)))

acc, i = 0, 0
seen = set()
while i not in seen:
    seen.add(i)
    name, val = insts[i]
    if name == 'nop': i += 1
    elif name == 'acc':
        acc += val
        i += 1
    elif name == 'jmp':
        i += val

print(acc)

