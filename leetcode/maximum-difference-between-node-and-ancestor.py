# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def solve(root, minVal = float('inf'),  maxVal = float('-inf')):

            if not root:
                return abs(maxVal - minVal)
            return max(solve(root.right, min(minVal, root.val), max(maxVal, root.val)), solve(root.left, min(minVal, root.val), max(maxVal, root.val)))
        return solve(root)
        