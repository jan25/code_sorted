
vow = 'aeiou'
def getVow(x, y):
    return vow[(x + y) % 5]

def makeString(n, m):
    chars = []
    for i in range(n * m):
        chars.append(getVow(i // n, i % n))
    return ''.join(chars)

def Solution(k):
    n, m = 5, 1
    while n * n <= k:
        if k % n == 0:
            m = k // n
            break
        n += 1
    if m == 1: return -1
    return makeString(n, m)

print (Solution(int(input())))