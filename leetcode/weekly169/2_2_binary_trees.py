'''
https://leetcode.com/contest/weekly-contest-169/problems/all-elements-in-two-binary-search-trees/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        h = []
        
        def traverse(r):
            if r is None: return
            h.append(r.val)
            traverse(r.left)
            traverse(r.right)
        
        traverse(root1)
        traverse(root2)
        
        heapq.heapify(h)
        sorted_h = []
        while len(h) > 0:
            sorted_h.append(heapq.heappop(h))
        
        return sorted_h
    