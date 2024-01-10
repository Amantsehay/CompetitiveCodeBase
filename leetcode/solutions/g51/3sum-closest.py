
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_dif = float('inf')
        ans = float('inf')
        for i, a in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                diff = a + nums[l] + nums[r] - target
                s = diff + target
                if min_dif > abs(diff):
                    ans = s
                    min_dif = min(abs(diff), min_dif)

                if diff > 0:
                    r -= 1
                elif diff < 0:
                    l += 1
                else:
                    return target
        return ans