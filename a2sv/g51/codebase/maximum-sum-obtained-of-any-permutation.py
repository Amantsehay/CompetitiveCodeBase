class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        n = len(nums)
        dp = [0]  * n 
        for i in range(len(requests)):
            start = requests[i][0]
            end = requests[i][1]
            dp[start] += 1
            if end + 1 < n:
                dp[end + 1] -= 1
        for i in range(1, n):
            dp[i] += dp[i - 1]
        dp.sort()
        nums.sort()
        ans = 0

        for i in range(n):
            ans += nums[i] * dp[i]
        return ans % (10**9 + 7)

        
        
        