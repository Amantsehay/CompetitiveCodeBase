class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # the basecase is when the length of the array is just one 
        memo = {}
        def dp( nums, start, end, turn):
            if start > end:
                return 0
            if (start, end, turn) in memo:
                return memo[(start, end, turn)]
            res = 0
            if turn == 1:
                res =  max(nums[start] + dp(nums, start + 1, end, 0), nums[end] +dp(nums, start, end - 1, 0))
            else:
                res =  min(dp(nums, start + 1, end, 1), dp(nums, start, end - 1, 1))

            memo[(start, end, turn)] = res
            return res

        
        n = len(nums)
        rslt = dp(nums, 0, n - 1, 1) 
        return rslt >= sum(nums) - rslt
        