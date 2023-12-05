class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = end = ans = 0
        while (end < len(nums)):
            if (nums[end] == 0):
                start = end + 1  
            ans = max(ans, end - start +1 )
            end += 1
        return ans
        
        