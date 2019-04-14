import sys

def _flush():
    sys.stdout.flush()

def Solution(n, m):
    max_seen = 0
    for _ in range(n):
        before = ['18' for _ in range(18)]
        print (' '.join(before)); _flush()
        after = list(map(int, input().split()))
        diff = 0
        for i in range(18): diff += after[i]
        max_seen = max(diff, max_seen)
    print (max_seen); _flush()
    int(input())

t, n, m = map(int, input().split())
for _ in range(t):
    Solution(n, m)