'''
https://leetcode.com/contest/weekly-contest-174/problems/maximum-product-of-splitted-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        mod = 10**9 + 7
        
        def multiply(root):
            if root is None: return 0
            root.val += multiply(root.right)
            root.val += multiply(root.left)
            return root.val
        
        product = multiply(root)
        
        def split(node):
            if node is None: return 0
            max_prod = max(split(node.right), split(node.left))
            if node.left:
                max_prod = max(max_prod, (root.val - node.left.val) * node.left.val)
            if node.right:
                max_prod = max(max_prod, (root.val - node.right.val) * node.right.val)
            return max_prod
                
        return split(root) % mod
                
