class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        nums  = [i for i in range(1, 10)]
        def dfs(idx, target, curr, k):

            if target < 0:
                return 
            if target == 0 and len(curr) == k:
                ans.append(curr)
                return
            for i in range(idx, len(nums)):
                if (i != idx and nums[i] == nums[i -1]):
                    continue
                dfs(i + 1, target - nums[i], curr +[nums[i]], k)
        dfs(0 ,n, [], k)


        return ans
        
        