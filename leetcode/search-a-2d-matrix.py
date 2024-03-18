class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def findArray():
            start, end = 0, len(matrix) - 1
            while start <= end:
                midd = (start + end) // 2 
                if matrix[midd][0] <= target <= matrix[midd][-1]:
                    return midd
                elif matrix[midd][0] > target:
                    end = midd - 1
                else:
                    start = midd + 1
            return - 1
        rslt = findArray()
        arr = matrix[rslt] if rslt != -1 else []
        i, j = 0, len(arr) - 1
        while i <= j:
            midd = (i + j)// 2
            if arr[midd] == target:
                return True
            if arr[midd] > target:
                j = midd - 1
            else:
                i = midd + 1
        return False
        