'''
https://leetcode.com/contest/weekly-contest-177/problems/validate-binary-tree-nodes/
'''
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        seen = set()
        edges = 0
        
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            if l in seen or r in seen: return False
            if l != -1: seen.add(l); edges += 1
            if r != -1: seen.add(r); edges += 1
        
        return edges == n - 1
        
