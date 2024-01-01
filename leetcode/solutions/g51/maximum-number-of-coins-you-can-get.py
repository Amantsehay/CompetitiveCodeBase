class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        n = len(piles)
        for i in range(n - 2, n // 3 - 1, -2):
            ans+=piles[i]
            i += 2
        return ans