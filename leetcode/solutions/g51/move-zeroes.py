class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = 0
        j = 0
        # i will only move after the swaping 

        while j < n:
            while i < n and nums[i] != 0:
                i += 1
            while j < i or (j < n and nums[j] == 0):
                j += 1
            if i < n and j < n :
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
                   


        