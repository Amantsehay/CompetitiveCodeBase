class Solution:
    def canJump(self, nums: List[int]) -> bool:

        

        n = len(nums)
        
        def solve(start, score):

            if start == n:
                return True
            if score < start:
                return False
            return solve(start + 1, max(score, start + nums[start]))
        return solve(0, 0)

        