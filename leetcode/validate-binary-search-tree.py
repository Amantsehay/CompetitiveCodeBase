# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def solve(root, minVal = float('-inf'),  maxVal = float('inf')):

            if not root:
                return True
            if  not (minVal < root.val < maxVal):
                return False
            return solve(root.right, root.val, maxVal) and solve(root.left, minVal, root.val)
        return solve(root)
       
        