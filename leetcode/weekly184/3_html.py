'''
https://leetcode.com/contest/weekly-contest-184/problems/html-entity-parser/
'''
class Solution:
    def entityParser(self, text: str) -> str:
        
        def replace(s, this, thatC):
            n = len(s)
            m = len(this)
            s = list(s)
            for i in range(n):
                if i + m > n: break
                if this == ''.join(s[i:i + m]):
                    for j in range(m): s[i + j] = "-"
                    s[i] = thatC
            return ''.join(s)
            
        pairs = [('&quot;', '\"'), ('&apos;', "'"), ('&amp;', '&'), ('&gt;', '>'), ('&lt;', '<'), ('&frasl;', '/')]
        s = text
        for p in pairs:
            s = replace(s, *p)
        return s.replace('-', '')
                    
