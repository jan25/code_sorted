import fileinput

lines = list(fileinput.input())
running, top = 0, []
for l in lines:
    l = l.strip()
    if l == "":
        top.append(running)
        top = sorted(top)[-3:]
        running = 0
        continue
    running += int(l)
top.append(running)
top = sorted(top)[-3:]

print(sum(top))
