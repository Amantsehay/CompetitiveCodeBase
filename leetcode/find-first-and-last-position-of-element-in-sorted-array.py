class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def last():
            i, j = 0, len(nums) - 1
            while i <= j:
                midd = (i + j) // 2 
                if nums[midd] > target:
                    j = midd  - 1
                else:
                    i = midd + 1
            return i
        def first():
            i, j = 0, len(nums) - 1
            while i <= j:
                midd = (i + j) // 2
                if nums[midd] >= target:
                    j = midd - 1
                else:
                    i = midd + 1
            return i
        return [first(), last() - 1] if nums[last() - 1] == target  else [-1, -1]