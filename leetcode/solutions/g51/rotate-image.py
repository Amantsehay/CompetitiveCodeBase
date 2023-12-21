class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
         
        """
        x1 = y1 = x2 = y2 = 0
        n = len(matrix)
        for i in range(2 * n - 1):
            self.tranverse(matrix, x1, y1, x2, y2)
            if (x1 >= n - 1):
                y1 += 1
            else:
                x1 += 1
            if (y2 >= n - 1):
                x2 += 1
            else:
                y2 += 1
        for mat in matrix:
            mat.reverse()
            
                

    def tranverse(self, matrix, x1, y1, x2, y2):
        n = len(matrix)
        while (x1  > x2 or y2 > y1):
            matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
            x1 -= 1
            y1 += 1
            x2 += 1
            y2 -=1 




        






        return matrix



    
        