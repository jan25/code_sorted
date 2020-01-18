'''
https://leetcode.com/contest/weekly-contest-171/problems/minimum-distance-to-type-a-word-using-two-fingers/

Dynamic Programming algorithm:
State - (L, R) L left finger position, R is right finger position
Here Invariant is R > L
Time and space - O(N ** 2)
'''
class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        
        def to_2d(c):
            i = ord(c) - ord('A')
            return (i // 6, i % 6)
        
        def diff(a, b):
            if a < 0: return 0
            a, b = to_2d(word[a]), to_2d(word[b])
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        cache = {}
        def cost(l, r):
            if r == n - 1: return 0
            if (l, r) not in cache:
                c = diff(r, r + 1) + cost(l, r + 1)
                c = min(c, diff(l, r + 1) + cost(r, r + 1))
                cache[(l, r)] = c
            return cache[(l, r)]
            
        return cost(-1, -1)
    