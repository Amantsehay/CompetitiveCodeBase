# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # this is a bradth first search 
        mp = {}

        def solve(depth, root):
            if not root:
                return depth
            if depth in mp:
                mp[depth].append(root.val)
            else: 
                mp[depth] = [root.val]
            solve(depth + 1, root.left)
            solve(depth + 1, root.right)
        solve(0, root)
        
        ans = []
        count = 0
        for key in mp:
            if count % 2:

                ans.append(mp[key][::-1])
            else:
                ans.append(mp[key])
            count += 1
        return ans
        

        