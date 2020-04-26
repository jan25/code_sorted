'''
https://leetcode.com/contest/weekly-contest-185/problems/reformat-the-string/
'''
class Solution:
    def reformat(self, s: str) -> str:
        alp = list(chr(c) for c in range(ord('a'), ord('z') + 1))
        num = list(map(str, range(10)))
        
        alpc = [c for c in s if c in alp]
        alpn = [c for c in s if c in num]
        print(alpc, alpn)
        if abs(len(alpc) - len(alpn)) > 1: return ''
        if len(alpc) > len(alpn):
            return ''.join(a[0] + a[1] for a in zip(alpc, alpn)) + alpc[-1]
        if len(alpn) > len(alpc):
            return ''.join(a[0] + a[1] for a in zip(alpn, alpc)) + alpn[-1]
        return ''.join(a[0] + a[1] for a in zip(alpn, alpc))
    
