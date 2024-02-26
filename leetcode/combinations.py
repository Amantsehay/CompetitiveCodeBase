class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(start, n, curr):
            if len(curr) == k:
                ans.append(curr[::])
                return 
            for i in range(start, n):
                curr.append(i + 1)
                backtrack(i + 1, n, curr)
                curr.pop()


        curr = []
        backtrack(0, n,curr)
        return ans