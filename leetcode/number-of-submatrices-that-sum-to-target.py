class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix[0]), len(matrix)

        for i in range(n):
            for j in range(1, m):
                matrix[i][j] += matrix[i][j - 1]

        ans = 0

        for i in range(m):
            for j in range(i, m):
                curr_sum = 0

                d = {0: 1}

                for row in range(n):
                    curr_sum += matrix[row][j] - (0 if i <= 0 else matrix[row][i - 1]) 
                    need = curr_sum - target 
                    if need in d:
                        ans += d[need]
                    d[curr_sum] = d.get(curr_sum, 0) + 1

        return ans



        

        


        


        return 0
        
        