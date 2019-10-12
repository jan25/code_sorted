'''
https://leetcode.com/contest/weekly-contest-157/problems/count-vowels-permutation/
'''

mod = 10 ** 9 + 7 
rules = {
    'a': 'e',
    'e': 'ai',
    'i': 'aeou',
    'o': 'iu',
    'u': 'a'
}
memo = { }

def dp(c, n):
    if n == 0: return 1
    if (c, n) not in memo:
        sol = 0
        for nc in rules[c]:
            sol += dp(nc, n - 1)
        memo[(c, n)] = sol % mod
    return memo[(c, n)]
    
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        count = 0
        for f in 'aeiou':
            count += dp(f, n - 1)
            count %= mod
        return count
    