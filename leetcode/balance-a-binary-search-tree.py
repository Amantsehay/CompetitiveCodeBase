# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.ls = []
        def inOrder(root):
            if not root:
                return 
            inOrder(root.left)
            self.ls.append(root.val)
            inOrder(root.right)
        inOrder(root)
        
        self.ls.sort()

        def construct(nums, start, end):
            if start > end:
                return None
            midd = (start  + end) // 2
            node = TreeNode(nums[midd])
            node.left = construct(nums, start, midd - 1)
            node.right = construct(nums, midd + 1, end)
            return node
        return construct(self.ls, 0, len(self.ls) - 1)
        