'''
https://leetcode.com/contest/weekly-contest-180/problems/balance-a-binary-search-tree/

THE DAY-STOUT-WARREN (DSW) ALGORITHM:
1. Convert tree into linear linked list
2. left rotate few times on linked list nodes to make it balanced

See here for example https://leetcode.com/problems/balance-a-binary-search-tree/discuss/541785

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def rightRotate(root):
            assert root.left is not None
            tmpRoot = root
            root = root.left
            tmpRoot.left = root.right
            root.right = tmpRoot
            return root
        
        def leftRotate(root):
            if root is None: return None
            if root.right is None: return root
            tmpRoot = root
            root = root.right
            tmpRoot.right = root.left
            root.left = tmpRoot
            return root
        
        def recLeftRotate(root, n):
            if root is None or n == 0: return root
            root = leftRotate(root)
            root.right = recLeftRotate(root.right, n - 1)
            return root
        
        def straighten(root):
            if root is None: return None, 0
            while root.left:
                root = rightRotate(root)
            root.right, nn = straighten(root.right)
            return root, nn + 1
        
        root, numNodes = straighten(root)
        initialRotations, twos = numNodes, 1
        while twos <= initialRotations:
            initialRotations -= twos
            twos <<= 1

        root = leftRotate(root)
        initialRotationRoot = root
        for _ in range(initialRotations - 1):
            initialRotationRoot.right = leftRotate(initialRotationRoot.right)
            initialRotationRoot = initialRotationRoot.right
        
        numNodes -= initialRotations
        while numNodes // 2 > 0:
            root = recLeftRotate(root, numNodes // 2)
            numNodes //= 2
        
        return root
    
