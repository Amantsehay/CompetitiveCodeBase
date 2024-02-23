# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # traversing at the same time 
        
        def solve(root1, root2):
            if not root1 and not root2:
                return True
            if (root2 and not root1) or( not root2 and root1):
                return False
            
            if root2.val != root1.val:
                return False

            return solve(root1.left, root2.right) and solve(root1.right, root2.left)
        return solve(root, root)

        