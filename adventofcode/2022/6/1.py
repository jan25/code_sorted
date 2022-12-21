import fileinput


def search(s, n=4):
    for i in range(len(s)):
        if len(set(s[i:i+n])) == n:
            return i + n
    assert False, 'not found'


def search2(s):
    return search(s, n=14)


l = list(fileinput.input())[0].strip()
print(search(l))
print(search2(l))
