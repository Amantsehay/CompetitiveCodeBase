class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #    if every diagonal has the same value 
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if (j < m - 1 and i < n - 1):
                    if (matrix[i][j] != matrix[i + 1][j + 1]):
                        return False
        return True




        