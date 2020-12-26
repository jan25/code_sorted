groups, group = [], []
with open('input') as f:
    for line in f:
        if line.strip() == "":
            groups.append(group)
            group = []
        else:
            group.append(line.strip())
if group: groups.append(group)

print(groups)

def common(g):
    if len(g) == 1: return len(g[0])
    return len(set(g[0]).intersection(*[set(l) for l in g[1:]]))

print(sum(common(g) for g in groups))