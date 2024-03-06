class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        arr = [float('-inf')] + arr + [float('-inf')]
        n = len(arr)
        for i in range(n):
            curr = arr[i]
            while stack and curr < stack[-1][1]:
                ind, val = stack.pop()
                ans = max(val * (i - stack[-1][0] - 1), ans)
            stack.append([i, curr])
        
        return ans % (10**9 + 7)


        
        