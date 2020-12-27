
insts = []
with open('input') as f:
    for inst in f:
        name, val = inst.split()
        insts.append((name, int(val)))

def try_this():
    acc, i = 0, 0
    seen = set()
    while i not in seen and i < len(insts):
        seen.add(i)
        name, val = insts[i]
        if name == 'nop': i += 1
        elif name == 'acc':
            acc += val
            i += 1
        elif name == 'jmp':
            i += val
    if i in seen: raise Exception("infinite loop")
    return acc

for i in range(len(insts)):
    name, val = insts[i]
    try:
        if name == 'jmp':
            insts[i] = ('nop', val)
        elif name == 'nop':
            insts[i] = ('jmp', val)
        print(try_this())
        break
    except Exception:
        print('wait for it..')
    insts[i] = (name, val)
    