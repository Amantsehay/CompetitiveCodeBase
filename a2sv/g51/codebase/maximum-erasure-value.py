class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # this is the subarray
        n = len(nums)
        l = 0
        ans = 0
        tot = 0
        count = {}
        for r in range(n):
            tot += nums[r]
            count[nums[r]] = count.get(nums[r], 0) + 1
            while l <= r and count[nums[r]] > 1:
                tot -= nums[l]
                count[nums[l]] -= 1
                l += 1
            ans = max(ans, tot)
        return ans




        