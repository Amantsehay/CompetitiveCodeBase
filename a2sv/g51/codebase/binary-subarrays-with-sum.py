class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # this is a prefix sum problem 
        count = {0: 1}
        ans = 0
        n = len(nums)
        curr = 0
        for i in range(n):
            curr += nums[i]
            need = curr - goal
            if need in count:
                ans += count[need]
            count[curr] = count.get(curr, 0) + 1
        return ans