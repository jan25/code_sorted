'''
https://leetcode.com/contest/weekly-contest-183/problems/longest-happy-string/
'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = list('abc')
        n = [a, b, c]
        i = [0, 1, 2]
        i.sort(key=lambda j: n[j])
        
        abc = ''.join(map(lambda j: s[j], i))
        
        fs = abc * n[i[0]] + abc[1:] * (n[i[1]] - n[i[0]])
        
        fs = list('-' + fs + '-')
        rem = n[i[2]] - n[i[1]]
        for i in range(1, len(fs) - 1):
            if rem <= 0: break
            if fs[i] == abc[-1]:
                fs[i] = abc[-1] * 2
                rem -= 1
            elif fs[i] == abc[0]:
                fs[i] = abc[0] + (abc[-1] * min(rem, 2))
                rem -= 2
        
        fs = abc[-1] * min(2, rem)  + ''.join(fs[1:-1])
        
        return fs
    
