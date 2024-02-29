class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        left_count = self.count_nodes(root.left)
        if k <= left_count:
            return self.kthSmallest(root.left, k)
        elif k == left_count + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - left_count - 1)
    
    def count_nodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)
