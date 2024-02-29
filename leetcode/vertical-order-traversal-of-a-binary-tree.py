# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = defaultdict(list)

        def solve(root, y, x):

            if not root:
                return 
            
            mp[y].append((root.val, x))
            solve(root.left, y - 1, x + 1)
            solve(root.right, y  + 1,x + 1)
          
        solve(root, 0, 0)
        ans = []
        
        for key in sorted(mp):
            ls = mp[key]
            ls = sorted(ls, key=lambda x: (x[1], x[0]))
            ans.append([x[0] for x in ls])
        print(mp)
        return ans
        