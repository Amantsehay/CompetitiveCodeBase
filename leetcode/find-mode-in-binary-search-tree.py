from collections import defaultdict

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mp = defaultdict(int)

        def solve(root):
            if not root:
                return 
            mp[root.val] += 1

            solve(root.left)
            solve(root.right)

        solve(root)

        max_freq = max(mp.values())
        modes = [key for key, freq in mp.items() if freq == max_freq]

        return modes
