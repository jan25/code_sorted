groups, group = [], []
with open('input') as f:
    for line in f:
        if line.strip() == "":
            groups.append(group)
            group = []
        else:
            group.append(line.strip())
if group: groups.append(group)

print(sum(len(set(''.join(g))) for g in groups))