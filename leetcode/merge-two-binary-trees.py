# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


        ans = TreeNode()

        def solve(root1, root2):

            if not root1 and not root2:
                return 
            if root1 and root2:
                new = TreeNode(root1.val + root2.val)
                new.left = solve(root1.left, root2.left)
                new.right = solve(root1.right, root2.right)
                return new
            if root1:
                new = TreeNode(root1.val)
                new.left = solve(root1.left, root2)
                new.right = solve(root1.right, root2)
                return new
            if root2:
                new = TreeNode(root2.val)
                new.left = solve(root1, root2.left)
                new.right = solve(root1, root2.right)
                return new
        return solve(root1, root2)
            


      
            

        


        