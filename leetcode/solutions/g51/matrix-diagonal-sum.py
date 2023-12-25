class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            ans += mat[i][i] + mat[i][n - i - 1]
            
        if n % 2 == 0:
            return ans
        return ans - mat[n//2][n//2]


        