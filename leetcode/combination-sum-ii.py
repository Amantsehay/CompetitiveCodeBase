class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # this is basically the combination one 

        ans = []
        nums.sort()
        print(nums)
        def dfs(idx, target, curr):
            if target < 0:
                return 
            if target == 0:
                ans.append(curr)
                return
            for i in range(idx, len(nums)):
                if i != idx and nums[i] == nums[i -1]:
                    continue
                dfs(i + 1, target - nums[i], curr +[nums[i]])
        dfs(0 ,target, [])

        return ans
        