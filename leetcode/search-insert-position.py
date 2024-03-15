class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l, h = 0, len(nums) - 1
        while l <= h:
            midd = (l + h) //2 
            if nums[midd] == target:
                return midd
            if nums[midd] > target:
                h = midd - 1
            else:
                l = midd + 1
        return l 
        