'''
https://leetcode.com/contest/weekly-contest-172/problems/print-words-vertically/
'''
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        n = max(len(w) for w in words)
        
        def make_vword(i):
            last_j = -1
            chrs = []
            for j, w in enumerate(words):
                if len(w) > i:
                    chrs.append(' ' * (j - last_j - 1))
                    chrs.append(w[i])
                    last_j = j
            return ''.join(chrs)
            
        return [make_vword(i) for i in range(n)]
    