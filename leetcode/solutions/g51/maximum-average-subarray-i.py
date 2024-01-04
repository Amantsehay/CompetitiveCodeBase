class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        tot = 0
        maxx = float('-inf')
        n = len(nums)
        for i in range(n):
            tot += nums[i]
            if i >= k - 1:
                maxx = max(maxx, tot/k)
                tot -= nums[i - k + 1]
        return maxx
        