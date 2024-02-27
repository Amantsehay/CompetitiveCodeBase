class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def backtrack(start, n, curr):
            if len(curr) == k:
                ans.append(curr[:])  
                return
            for i in range(start, n + 1):
                curr.append(i)
                if len(curr) + (n - start + 1) >= k:
                    backtrack(i + 1, n, curr)
                curr.pop()

        backtrack(1, n, [])
        return ans
