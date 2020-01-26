'''
https://leetcode.com/contest/weekly-contest-172/problems/delete-leaves-with-a-given-value/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if root is None: return root
        
        def remover(root):
            l, r = True, True
            if root.left is not None: l = remover(root.left)
            if root.right is not None: r = remover(root.right)
            if l: root.left = None
            if r: root.right = None
            if root.left is None and root.right is None:
                return root.val == target
            return False
        
        return None if remover(root) else root
    