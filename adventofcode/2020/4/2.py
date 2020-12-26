
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

'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''
def ok(kv):
    req = {'iyr', 'byr', 'pid', 'hcl', 'ecl', 'hgt', 'eyr'}
    for k, _ in kv.items():
        if k != 'cid':
            if k not in req: return False
            req.remove(k)

    if req: return False

    def chk(k, l, mini, maxi, val=None):
        digs = val or kv[k]
        if not digs.isdigit() or len(digs) != l: return False
        val = int(digs)
        return mini <= val <= maxi

    if not chk('byr', 4, 1920, 2002): return False
    if not chk('iyr', 4, 2010, 2020): return False
    if not chk('eyr', 4, 2020, 2030): return False
    
    hgt, unit = kv['hgt'][:-2], kv['hgt'][-2:]
    if unit not in {'cm', 'in'}: return False
    if unit == 'cm' and not chk(None, 3, 150, 193, hgt): return False
    if unit == 'in' and not chk(None, 2, 59, 76, hgt): return False

    pid = kv['pid']
    if not pid.isdigit() or len(pid) != 9: return False

    ecl = kv['ecl']
    if ecl not in set('amb blu brn gry grn hzl oth'.split()): return False

    hcl = kv['hcl']
    if len(hcl) != 7 or hcl[0] != '#' or not hcl[1:].isalnum(): return False

    return True

valid = 0
for p in passports:
    kvs = dict()
    for kv in p.split():
        k, v = kv.split(':')
        kvs[k] = v
    if ok(kvs): valid += 1

print(valid)