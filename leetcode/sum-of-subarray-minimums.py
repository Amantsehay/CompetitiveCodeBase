class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        ans = 0
        arr = [float('-inf')] + arr  + [float('-inf')]
        n = len(arr)
        for i in range(n):
            curr = arr[i]
            while stack and curr < stack[-1][1]:
                ind, val = stack[-1]
                stack.pop()
                left = ind - stack[-1][0]
                right =  i  - ind
                ans += val * left * right
            stack.append([i, curr])
        
        return ans % (10**9 + 7)