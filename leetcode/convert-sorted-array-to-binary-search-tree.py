# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # Is this the parted with 
        #
        
        def solve(start, end):

            if start > end:
                return None
            midd = (start + end)//2  
            # midd += 0 if (start + end) % 2 else 1
            node = TreeNode(nums[midd])
            node.left = solve(start, midd - 1)
            node.right = solve(midd + 1,end)
            return node
        return solve(0, len(nums) - 1)

        
        