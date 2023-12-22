class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        start = 0
        end = n  - 1
        if n < 3:
            return False
        for i in range(n):
            if start < n - 1 and arr[start] < arr[start + 1]:
                start += 1
            if end > 0 and arr[end] < arr[end - 1]:
                end -= 1
        return end == start and end != n - 1 and start != 0
            
