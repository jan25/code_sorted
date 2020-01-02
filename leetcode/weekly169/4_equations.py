'''
https://leetcode.com/contest/weekly-contest-169/problems/verbal-arithmetic-puzzle/

Bruteforce algorithm using backtracing

Potential ways to prune:
- most significant positions won't have 0 digit assigned
- ones position digits can be used for early pruning
- similar to above higher position digits can be used for pruning too

This implementation
- Using the first pruning method
- use coeffecients trick to quickly evaluate potential solution
- more bitwise operations for faster backtracing

This implementation gives TLE on Leetcode, perhaps because of tight limits on Python3

'''
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        
        def ctoi(c):
            return ord(c) - ord('A')
        
        all_chars = result
        for w in words: all_chars += w
        acu = list(set(map(ctoi, all_chars)))
        print(acu)
        
        non_zeros = (1 << ctoi(result[0]))
        for w in words:
            non_zeros |= (1 << ctoi(w[0]))
        
        coeffs = {}
        def add_coeff(w, neg=False):
            mult = -1 if neg else 1
            for c in w[::-1]:
                if c in coeffs:
                    coeffs[ctoi(c)] += mult
                else:
                    coeffs[ctoi(c)] = mult
                mult *= 10

        add_coeff(result, neg=True)
        for w in words: add_coeff(w)
        
        def assign(i=0, tot=0, used=0):
            if i >= len(acu):
                return tot == 0
            
            cache_s = False
            c = acu[i]
            for d in range(10):
                if (used & (1 << d)) > 0: continue
                if d == 0 and ((1 << c) & non_zeros) > 0: continue
                cache_s = cache_s or assign(i + 1, tot + coeffs[c] * d, used | (1 << d))
                
            return cache_s
        
        return assign()
