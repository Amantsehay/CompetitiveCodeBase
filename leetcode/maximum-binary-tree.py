# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:


        if not nums:
            return None
        
        maxIndex = nums.index(max(nums))

        newNode = TreeNode(nums[maxIndex])
        newNode.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        newNode.right = self.constructMaximumBinaryTree(nums[maxIndex + 1:])
        return newNode
        