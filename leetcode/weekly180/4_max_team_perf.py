'''
https://leetcode.com/contest/weekly-contest-180/problems/maximum-performance-of-a-team/
'''
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = (10**9) + 7
        
        si = list(range(n))
        si.sort(key=lambda i: speed[i])
        i2si = {sii: i for i, sii in enumerate(si)}
        
        ei = list(range(n))
        ei.sort(key=lambda i: efficiency[i])
        
        kcurr = n - k
        ksum = sum(speed[si[i]] for i in range(kcurr + 1, n))
        kelems = k - 1
        perf = 0
        
        for i in ei:
            while kelems < k - 1 and kcurr >= 0:
                if kcurr < n and speed[si[kcurr]] != 0:
                    kelems += 1
                    ksum += speed[si[kcurr]]
                kcurr -= 1
            while kcurr >= 0 and speed[si[kcurr]] == 0:
                kcurr -= 1
            
            if i2si[i] <= kcurr:
                perf = max(perf, (ksum + speed[i]) * efficiency[i])
                speed[i] = 0
            else:
                extra_sum = 0 if kcurr < 0 else speed[si[kcurr]]
                perf = max(perf, (extra_sum + ksum) * efficiency[i])
                kelems -= 1
                ksum -= speed[i]
                speed[i] = 0
                
        return perf % mod
    
