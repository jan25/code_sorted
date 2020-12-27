#!/usr/bin/python3
import fileinput

a, b = [], []
lines = a
for line in fileinput.input():
    if line.strip() == "":
        a = lines
        lines = b
    elif line.strip().isdigit():
        lines.append(int(line.strip()))

print(a, b)

step = 0
while a and b:
    nexta, nextb = [], []
    for vala, valb in zip(a, b):
        if vala > valb:
            nexta.append(vala)
            nexta.append(valb)
        else:
            nextb.append(valb)
            nextb.append(vala)
    minl = min(len(a), len(b))
    a, b = a[minl:] + nexta, b[minl:] + nextb
    step += 1
    if step % 10000: print(step)

print(a, b)

print(sum((i + 1) * val for i, val in enumerate(reversed(a or b))))