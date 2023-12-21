class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        ans = [[0] * n for i in range(m)]
        for i in range(n):
            for j in range(m):
                ans[j][i] = matrix[i][j]
        return ans

        