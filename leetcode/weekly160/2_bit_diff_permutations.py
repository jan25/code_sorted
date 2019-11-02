'''
https://leetcode.com/contest/weekly-contest-160/problems/circular-permutation-in-binary-representation/
'''
class Solution:
    def make(self, n):
        if n == 1: return [0, 1]
        a = list(map(lambda x: (x << 1), self.make(n - 1)))
        a = a + list(map(lambda x: (x | 1), a[::-1]))
        return a
    
    def circularPermutation(self, n: int, start: int) -> List[int]:
        a = self.make(n)
        print (a)
        for i in range(len(a)):
            if a[i] == start:
                return a[i:] + a[:i]
            