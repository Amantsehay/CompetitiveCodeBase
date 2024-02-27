# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        

        def solve(root, curr, ans):
            if not root:
                return 0
            curr += str(root.val)
            if not root.left and not root.right:
                ans += int(curr)
                return ans
            left = solve(root.left, curr, ans)
            right = solve(root.right, curr, ans)

            return left + right

        return solve(root, "", 0)
        


        