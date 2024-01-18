class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot = sum(nums)

        prefix = 0
        for i in range(len(nums)):
            if tot - prefix - nums[i] == prefix:
                return i
            prefix += nums[i]
        return -1
        