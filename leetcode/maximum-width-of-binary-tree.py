# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        queue = deque()

        queue.append((root,1))
        ans = 0
        while queue:

            l = len(queue)
            start = queue[0][1]

            for i in range(l):
                node, curr  = queue.popleft()
                print(curr)
                ans = max(ans, curr - start + 1)
                
                if node.left:
                    queue.append((node.left, 2 * curr))
                if node.right:
                    queue.append((node.right, 2 * curr + 1))
        return ans





        