class Solution:
    def longestSubarray(self, nums):
        zeros = 0
        n = len(nums)
        l = 0
        ans = 0

        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            while l < n and zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            ans = max(i - l, ans)

        return ans
