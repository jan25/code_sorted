'''
https://leetcode.com/contest/weekly-contest-167/problems/sequential-digits/
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        sd = []
        
        def add(digs):
            a = int(''.join(map(str, digs)))
            if a < low or a > high: return
            sd.append(a)
        
        def f(digs=[]):
            if len(digs) > 9: return
            if len(digs) > 0 and digs[-1] == 10: return
            if len(digs) == 0:
                for d in range(1, 10):
                    digs.append(d)
                    f(digs)
                    digs.pop()
            else:
                add(digs)
                digs.append(digs[-1] + 1)
                f(digs)
                digs.pop()
        
        f()
        return sorted(sd)
    