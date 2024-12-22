import re
import fileinput

stacks = []


def add_stack(cells):
    for i, c in enumerate(cells):
        if i == len(stacks):
            stacks.append([])
        if c[1] != '.':
            stacks[i] = [c[1]] + stacks[i]


def operate(many, src, dst):
    src -= 1
    dst -= 1
    stacks[dst] += stacks[src][-many:][::-1]
    stacks[src] = stacks[src][:-many]


for l in fileinput.input():
    print(l.strip().replace(' ' * 4, ' [.]', -1))
    cells = re.findall(
        r"[A-Z\.\[\]]+", l.strip().replace(' ' * 4, ' [.]', -1))
    if cells:
        add_stack(cells)
        continue
    if 'move' not in l:
        continue

    op = re.findall(r"\w+", l.strip())
    operate(*list(map(int, op[1::2])))


print(''.join(s[-1] for s in stacks))
