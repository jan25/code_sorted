
def Solution(signs, n):
    mn = [(s[0] + s[1], s[0] - s[2]) for s in signs]
    
    
    return (0, 0)

for t in range(int(input())):
    n = int(input())
    signs = [list(map(int, input().split())) for _ in range(n)]
    s = Solution(signs, n)
    print ('Case #%d: %d %d' % (t + 1, s[0], s[1]))
