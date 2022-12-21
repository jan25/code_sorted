import fileinput


def chr_prio(c: str) -> int:
    if c.islower():
        return 1 + ord(c) - ord('a')
    return 26 + chr_prio(c.lower())


def prio(l: str) -> int:
    n = len(l) // 2
    diff = set(l[:n]).intersection(set(l[n:]))
    return sum(chr_prio(c) for c in diff)


print(sum(prio(l.strip()) for l in fileinput.input()))
