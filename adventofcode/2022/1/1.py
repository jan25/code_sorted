import fileinput

lines = list(fileinput.input())
best, running = 0, 0
for l in lines:
    l = l.strip()
    if l == "":
        best = max(best, running)
        running = 0
        continue
    running += int(l)
print(best)
