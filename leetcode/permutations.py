class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(curr, used):
            if len(curr) == len(nums):
                ans.append(curr[::])
                return 
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    backtrack(curr, used)
                    used[i] = False
                    curr.pop()

        used = [False] * len(nums)
        curr = []
        backtrack(curr, used)
        return ans

        