'''
https://leetcode.com/contest/weekly-contest-160/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def bitty(a):
            if sorted(list(set(a))) != sorted(list(a)):
                return None
            x = 0
            for c in a:
                x |= 1 << (ord(c) - 97)
            return x
        
        def bits(a):
            n = 0
            while a > 0:
                if a & 1 > 0: n += 1
                a >>= 1
            return n
        
        arrr = list(filter(lambda x: x is not None, map(bitty, arr)))
        
        maxl = 0
        n = len(arrr)
        for mask in range(1 << n):
            an = 0
            for i in range(n):
                if mask & (1 << i):
                    if arrr[i] & an > 0:
                        an = 0; break
                    an |= arrr[i]
            maxl = max(bits(an), maxl)
        return maxl
    