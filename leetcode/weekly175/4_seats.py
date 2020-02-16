'''
https://leetcode.com/contest/weekly-contest-175/problems/maximum-students-taking-exam/
'''
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        n, m = len(seats), len(seats[0])
        
        rows = []
        for r in seats:
            br = 0
            for s in r:
                br <<= 1
                if s == '#': br |= 1
            rows.append(br)
        
        def is_ok_arrangement(pr, cr, row):
            if row & cr > 0: return False
            if pr & (cr << 1) > 0: return False
            if pr & (cr >> 1) > 0: return False
            if cr & (cr << 1) > 0 or cr & (cr >> 1) > 0: return False
            return True
        
        def next_bits(size):
            bits = (1 << size) - 1
            while bits >= 0:
                yield bits
                bits -= 1
        
        cache = {}
        def seat(ri, pr=0):
            if ri < 0: return 0
            if (ri, pr) not in cache:
                max_seated = 0
                for cr in next_bits(m):
                    if is_ok_arrangement(pr, cr, rows[ri]):
                        max_seated = max(max_seated, bin(cr).count('1') + seat(ri - 1, cr))
                cache[(ri, pr)] = max_seated
            return cache[(ri, pr)]
    
        return seat(n - 1)
                
            