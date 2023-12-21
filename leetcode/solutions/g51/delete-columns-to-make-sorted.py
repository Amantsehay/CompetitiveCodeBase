class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        n = len(strs)
        m = len(strs[0])
        for i in range(m):
            for j in range(n - 1):
                if (strs[j][i] > strs[j + 1][i]):
                    count += 1
                    break
        return count
        