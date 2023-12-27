class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        u = list(nums)
        nums.sort()
        s = {}
        
        for i, num in enumerate(nums):
            if num not in s:
                s[num] = i
        return [s[num] for num in u]

