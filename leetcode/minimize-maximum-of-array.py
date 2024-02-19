class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # this is greedy
        minn = min(nums)
        maxx = max(nums)
        while minn < maxx:
            mid = minn + (maxx - minn ) //2
            if self.canPartition(nums, mid):
                maxx = mid
            else:
                minn = mid + 1
        return minn

    def canPartition(self, nums, mid):
        if (mid < nums[0]):
            return False
        diff = 0
        for num in nums:
            diff += mid - num
            if diff < 0:
                return False
        return True
