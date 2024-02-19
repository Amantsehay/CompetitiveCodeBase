class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        mp = {}
        n = len(arr)
        for i in range(n):
            curr = arr[i]
            while stack and curr < stack[-1][1]:
                ind = stack[-1][0]
                mp[ind] = i -1
                stack.pop()
            stack.append([i, curr])
        stack = []
        mp2 = {}
        for i in range(n -1, -1, -1):
            curr = arr[i]
            while stack and curr <= stack[-1][1]:
                ind = stack[-1][0]
                mp2[ind] = i + 1
                stack.pop()
            stack.append([i, curr])
        ans = 0
        print(mp2, mp)
        for i in range(n):
            ans += (i - mp2.get(i, 0) + 1) * arr[i] * (mp.get(i, n - 1)  - i  + 1)
        return ans % (10**9 + 7)


