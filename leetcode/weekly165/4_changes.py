'''
https://leetcode.com/contest/weekly-contest-165/problems/palindrome-partitioning-iii/

Dynamic programming algorithm -
dp(string_index, remaining_k) = SUM dp(string_index + x, remaining_k - 1) for x in [string_index + 1, N]
This would normally take N ** 4 steps
We could speed it up with another lookup table - it tells number of changes required for s[i, j] substring
'''
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        
        def changes(i, j):
            ch = 0
            while i < j:
                if s[i] != s[j]:
                    ch += 1
                i += 1; j -= 1
            return ch
        
        # this is just to speed up look up later
        # dynamic programming algorithm
        pair_cache = {}
        for i in range(n):
            for j in range(n):
                pair_cache[(i, j)] = changes(i, j)
                
        sol_cache = {}
        def sol(i, k):
            if k == 0:
                if i == n: return 0
                else: return math.inf
            if i == n: return math.inf
            if (i, k) not in sol_cache:
                minch = math.inf
                for j in range(i, n):
                    ch = pair_cache[(i, j)]
                    minch = min(minch, ch + sol(j + 1, k - 1))
                sol_cache[(i, k)] = minch
            return sol_cache[(i, k)]
    
        return sol(0, k)
            