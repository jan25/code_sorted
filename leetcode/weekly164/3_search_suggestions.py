'''
https://leetcode.com/contest/weekly-contest-164/problems/search-suggestions-system/
'''
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        sp = sorted(products)
        
        p = []
        i, j = 0, n - 1
        for ic, c in enumerate(searchWord):
            while i < n and i <= j and (ic >= len(sp[i]) or sp[i][ic] != c): i += 1
            while j >= 0 and i <= j and (ic >= len(sp[j]) or sp[j][ic] != c): j -= 1
            if i <= j: p.append(sp[i:min(i + 3, j + 1, n)])
            else: p.append([])

        return p
        