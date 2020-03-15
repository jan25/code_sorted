# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def check(root, head):
            if head is None: return True
            if root is None: return False
            if root.val != head.val: return False
            return check(root.left, head.next) or check(root.right, head.next)
        
        def dfs(root):
            if root is None: return False
            return check(root, head) or dfs(root.left) or dfs(root.right)
        
        return dfs(root)
    
