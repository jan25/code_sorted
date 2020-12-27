
passports, lines = [], []
while True:
    try:
        line = input().strip()
        if line == "":
            passports.append(' '.join(lines))
            lines = []
        else:
            lines.append(line)
    except Exception:
        if lines:
            passports.append(' '.join(lines))
        break

valid = 0
for p in passports:
    req = {'iyr', 'byr', 'pid', 'hcl', 'ecl', 'hgt', 'eyr'}
    for kv in p.split():
        k, _ = kv.split(':')
        if k in req: req.remove(k)
    if not req: valid += 1

print(valid)