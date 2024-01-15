class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using bucct sort 
        s = {}
        for num in nums:
            s[num] = s.get(num, 0) +1
        i = 0
        while i < (s.get(0, 0)):
            nums[i] = 0
            i+=1
        while i < s.get(0, 0) + s.get(1,0):
            nums[i] = 1
            i+=1
        while i < s.get(0, 0) + s.get(1, 0) + s.get(2, 0):
            nums[i] = 2
            i+=1
