class Solution:
    def findMin(self, nums: List[int]) -> int:
        # I'm gonna worry about the last element 

        l, h = 0, len(nums)
        while l <= h:
            midd = (l + h) // 2 
            if nums[midd] > nums[-1]:
                l = midd + 1
            else:
                h = midd - 1
        return nums[l]
        