class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        prefix = [[0] * (1 + m) for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                prefix[i][j] = prefix[i][j - 1] + grid[i][j - 1]
        ans = 0
        print(prefix)
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                rslt =  prefix[i - 1][j + 2] - prefix[i - 1][j - 1]
                rslt += prefix[i + 1][j + 2] - prefix[i + 1][j - 1]
                ans = max(ans, grid[i][j] + rslt)
        return ans

            


        